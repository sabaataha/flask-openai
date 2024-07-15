from flask import Flask, request, jsonify
from db.db_init import init_db, db
from services import handle_ask_question, fetch_questions
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route("/")
def hello_world():
    return "<p>This is an OpenAI powered app!</p>"

@app.route("/ask", methods=['POST'])
def ask_question():
    data = request.get_json()
    response, status = handle_ask_question(data)
    return jsonify(response), status

@app.route("/questions", methods=['GET'])
def get_questions():
    response, status = fetch_questions()
    return jsonify(response), status

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
