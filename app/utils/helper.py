from app.extensions import db
from flask import Blueprint
import json, datetime, time, random, logging
from app.models.event import Event, MetricType
from sqlalchemy.exc import SQLAlchemyError

bp = Blueprint('health', __name__, url_prefix='/api/v1')

logger = logging.getLogger(__name__)

def generate_event_stream(interval_secs=1, max_duration_secs=60):
    
    start_time = time.time()
    
    while True:
        current_time = time.time()
        if current_time - start_time > max_duration_secs:
            # Expire connection after max_duration_seconds
            final_message = {
                "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
                "type": "stream_end",
                "message": "Stream expired. Please reconnect for more data."
            }
            yield f"data: {json.dumps(final_message)}\n\n"
            break
        
        metric_type = random.choice(list(MetricType))
        
        if metric_type == MetricType.TEMPERATURE:
            value = round(random.uniform(20.0, 30.0), 2)  
        elif metric_type == MetricType.CPU_USAGE:
            value = round(random.uniform(0.0, 100.0), 2) 
        elif metric_type == MetricType.FINANCIAL_STOCK:
            value = round(random.uniform(100.0, 1000.0), 2)  
        
        current_timestamp = datetime.datetime.utcnow().isoformat() + "Z",
        event = {
            "timestamp": current_timestamp,
            "metric": metric_type.value,  # Use the string value from the enum
            "value": value
        }

        try: 
            db.session.add(Event(
                        timestamp=current_timestamp,
                        metric=metric_type,
                        value=value
                    )) 
            db.session.commit()
        except SQLAlchemyError as e:
            logger.error(f"Database error while saving event: {str(e)}")
            db.session.rollback()
        except Exception as e:
            logger.exception("Unexpected error while saving event")
            db.session.rollback()

        yield f"data: {json.dumps(event)}\n\n"
        time.sleep(interval_secs)  # emit every 1 second