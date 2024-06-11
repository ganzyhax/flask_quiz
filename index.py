from flask import Flask, render_template, request

app = Flask(__name__)

# Define your quiz questions and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "Berlin", "London", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    # Add more questions here
]

@app.route('/')
def quiz():
    return render_template('quiz.html', questions=quiz_questions)

@app.route('/result', methods=['POST'])
def result():
    score = 0
    answers = request.form
    for question in quiz_questions:
        if answers.get(question["question"]) == question["answer"]:
            score += 1
    return render_template('result.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)
