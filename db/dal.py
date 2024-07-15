from db.db_init import db
from db.models import Question

def add_question(question_text, answer_text):
    new_question = Question(question=question_text, answer=answer_text)
    db.session.add(new_question)
    db.session.commit()

def get_all_questions():
    questions = Question.query.all()
    questions_list = [{'id': q.id, 'question': q.question, 'answer': q.answer} for q in questions]
    return questions_list
