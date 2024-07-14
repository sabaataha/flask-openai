from flask import Flask , request, jsonify


app = Flask(__name__)



@app.route("/")
def hello_world():
    return "<p>This is an OpenAI powered app !</p>"


@app.route("/ask" ,  methods=['POST'])
def ask_question():
    data = request.get_json()
    question_text = data.get('question')
    
    if not question_text:
        return jsonify({'error': 'No question provided'}), 400
    return jsonify({'question_text': question_text}), 200



    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)