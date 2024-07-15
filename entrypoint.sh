#!/bin/sh

wait_for_postgres() {
    until PGPASSWORD='1234' psql -h "$DATABASE_HOST" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
        echo "PostgreSQL is unavailable - sleeping"
        sleep 1
    done
    echo "PostgreSQL is up"
}
wait_for_postgres

alembic upgrade head

flask run --host=0.0.0.0 --port=5001
