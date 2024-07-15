from db.db_init import db  

class Question(db.Model):
    __tablename__ = 'questions'  
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text)
    answer = db.Column(db.Text)
