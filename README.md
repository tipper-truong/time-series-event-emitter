# Time Series Event Emitter

## Packages needed to run app 
- Docker
- Python

# Commands
## How to build app 
- docker-compose up --build
 
## Access PostgreSQL DB in Docker
- docker exec -it time-series-event-emitter-db-1 psql -U postgres -d metrics

# APIs 
- Get health status
  - curl http://127.0.0.1:3000/api/v1/health
- Stream event
  - curl -N http://127.0.0.1:3000/api/v1/stream
- Get history
  - curl http://127.0.0.1:3000/api/v1/history
    - Defaults to returning 10 events
  -  curl "http://127.0.0.1:3000/api/v1/history?limit=12"
    - limit = return N events   
