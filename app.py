from flask import Flask , request, jsonify
from flask_sqlalchemy import SQLAlchemy
from openai import OpenAI
from db.db_init import init_db, db  
from db.models import Question 
import os  ,openai , psycopg2


app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()


@app.route("/")
def hello_world():
    return "<p>This is an OpenAI powered app !</p>"


@app.route("/ask" ,  methods=['POST'])
def ask_question():
    data = request.get_json()
    question_text = data.get('question')
    
    if not question_text:
        return jsonify({'error': 'No question provided'}), 400
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question_text}]
        )
        answer_text = response.choices[0].message.content
        new_question = Question(question=question_text, answer=answer_text)
        db.session.add(new_question)
        db.session.commit()
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    return jsonify({'answer_text': answer_text}), 200



    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)