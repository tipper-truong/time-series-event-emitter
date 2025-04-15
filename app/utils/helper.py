import json, datetime, time, random
from app.models.event import MetricType

import json, datetime, time, random
from app.models.event import MetricType

def generate_event_stream(max_duration_seconds=60):
    
    start_time = time.time()
    
    while True:
        current_time = time.time()
        if current_time - start_time > max_duration_seconds:
            # Expire connection after max_duration_seconds
            final_message = {
                "timestamp": datetime.utcnow().isoformat() + "Z",
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
        
        event = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "metric": metric_type.value,  # Use the string value from the enum
            "value": value
        }
        
        yield f"data: {json.dumps(event)}\n\n"
        time.sleep(1)  # emit every 1 second