#!/bin/sh

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL to be ready..."
while ! nc -z db 5432; do
    sleep 0.1
done

# Drop and recreate database
echo "Dropping and recreating database..."
PGPASSWORD=postgres psql -h db -U postgres -d postgres -c "DROP DATABASE IF EXISTS metrics;"
PGPASSWORD=postgres psql -h db -U postgres -d postgres -c "CREATE DATABASE metrics;"

# Initialize migrations if they don't exist
if [ ! -d "migrations" ]; then
    echo "Initializing migrations directory..."
    flask db init
fi

# Create fresh migration
echo "Creating new migration..."
flask db migrate -m "Initial migration"

# Apply migration
echo "Applying migration..."
flask db upgrade

# Start the Flask application
echo "Starting Flask application..."
flask run --host=0.0.0.0 --port=3000 