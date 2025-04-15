from app.extensions import db
from flask import Blueprint, Response, stream_with_context
from http import HTTPStatus
from app.utils.helper import generate_event_stream
import json, datetime
from flask import request
from sqlalchemy import desc
from app.models.event import Event

bp = Blueprint('health', __name__, url_prefix='/api/v1')

### API ENDPOINTS ###
@bp.route('/health', methods=['GET'])
def health():
    response_data = {
        "message": "healthy",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",  # UTC timestamp
    }
    return Response(
        json.dumps(response_data),
        status=HTTPStatus.OK,
        mimetype="application/json"
    )

@bp.route('/stream', methods=['GET'])
def stream():
    return Response(stream_with_context(generate_event_stream()), content_type='text/event-stream')

@bp.route('/history', methods=['GET'])
def history():
    try:
        limit = int(request.args.get('limit', 10))
    except ValueError:
        return Response(
            json.dumps({"error": "Invalid limit parameter. Must be a positive integer."}),
            status=400,
            mimetype="application/json"
        )
    
    events = db.session.query(Event).order_by(desc(Event.timestamp)).limit(limit).all()
    return Response(
            json.dumps({"events": events.to_dict(), "count": len(events)}),
            status=HTTPStatus.OK,
            mimetype="application/json"
        )