
## Flask-OpenAI Setup

### Create a Python Virtual Environment and Install Required Packages, this only sets your flask app without db:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### Alembic for Migrations

#### Create Migration

```bash
alembic revision --autogenerate -m "YOUR COMMENT"
```

#### Apply Migration to Database

```bash
alembic upgrade head
```

### To start the application using Docker Compose:

```bash
docker compose  up --build
```

The app is now available on your localhost at the port specified by `${APP_PORT}` in your `.env` file.

### Clean Up

To stop and remove the Docker containers:

```bash
docker compose down 
```

## Testing

Run the `run_test.sh` in tests folder:

```bash
cd tests
./run_tests.sh
```

- Exit code `0`: Passed all the tests
- Exit code `1`: Failed in at least one test

