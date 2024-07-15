import openai
import os
from db.dal import add_question, get_all_questions

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_answer_from_openai(question_text):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question_text}]
    )
    return response.choices[0].message.content

def handle_ask_question(data):
    question_text = data.get('question')
    if not question_text:
        return {'error': 'No question provided'}, 400

    try:
        answer_text = get_answer_from_openai(question_text)
        add_question(question_text, answer_text)
    except Exception as e:
        return {'error': str(e)}, 500

    return {'answer_text': answer_text}, 200

def fetch_questions():
    try:
        questions_list = get_all_questions()
        return questions_list, 200
    except Exception as e:
        return {'error': str(e)}, 500
