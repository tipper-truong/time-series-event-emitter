from app.extensions import db
from flask import Blueprint, Response, stream_with_context
from http import HTTPStatus
from app.utils.helper import generate_event_stream
import json, datetime
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