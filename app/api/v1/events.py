from app.extensions import db
from flask import Blueprint, Response
from http import HTTPStatus
import json, datetime, time, random 
from app.utils.helper import generate_event_stream
bp = Blueprint('health', __name__, url_prefix='/api/v1')

### API ENDPOINTS ###
@bp.route('/health', methods=['GET'])
def health():
    response_data = {
        "message": "healthy",
        "timestamp": datetime.utcnow().isoformat() + "Z",  # UTC timestamp
    }
    return Response(
        json.dumps(response_data),
        status=HTTPStatus.OK,
        mimetype="application/json"
    )

@bp.route('/stream', methods=['GET'])
def stream():
    return Response(generate_event_stream(), content_type='text/event-stream')