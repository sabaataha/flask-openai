#!/bin/bash

# Default values

DB_URL=${1:-"localhost"}
DB_PORT=${2:-"5432"}


# Step 1: Create and activate the virtual environment if it doesn't exist
if [ ! -d "myenv" ]; then
    python3 -m venv myenv
fi

source myenv/bin/activate

# Step 2: Install the dependencies
pip install --upgrade pip
pip install -r requirements.txt

export HOST_URL
export DATABASE_HOST="$DB_URL"
export DATABASE_PORT="$DB_PORT"
export DATABASE_NAME="$POSTGRES_DB"
export DATABASE_USER="$POSTGRES_USER"
export DATABASE_PASSWORD="$POSTGRES_PASSWORD"
export APP_PORT_FLASK
# Step 3: Run the tests
pytest test.py

# Step 4: Deactivate virtual environment after tests run
deactivate

