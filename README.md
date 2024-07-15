# flask-openai

* create a Python virtual environment and install all the required packages
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


# alembic for migration
* create migration
```bash
alembic revision --autogenerate -m "YOUR COMMENT"
```
* push the migration to database
```bash
alembic upgrade head
```