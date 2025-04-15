from app.extensions import db
from flask import Blueprint, Response
from http import HTTPStatus
import json, datetime

bp = Blueprint('health', __name__, url_prefix='/api/v1')

### API ENDPOINTS ###
@bp.route('/health', methods=['GET'])
def health():
    response_data = {
        "message": "healthy",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"  # UTC timestamp
    }
    return Response(
        json.dumps(response_data),
        status=HTTPStatus.OK,
        mimetype="application/json"
    )