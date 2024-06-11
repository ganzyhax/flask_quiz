from flask import Flask, render_template, request

app = Flask(__name__)

# Define your quiz questions and answers
quiz_questions = [
    {
        "question": '''useEffect(() => {
        fetch('https://api.example.com/data')
            .then(response => response.json())
            .then(data => setData(data));
    }, []);

    return (
        <div>
            {data ? JSON.stringify(data) : 'Loading...'}
        </div>
    );
}
export default DataFetcher;
''',
        "options": ["a) useEffect без пустого массива", "b) useEffect с пустым массивом", "c) useEffect с объектом", "d) useEffect с функцией"],
        "answer": "c) useEffect с объектом"
    },
    {
        "question": "Какое из следующих утверждений о hook useEffect верно?",
        "options": ["a) useEffect вызывается до рендера компонента", "b) useEffect вызывается после каждого рендера компонента", "c) useEffect нельзя использовать в функциональных компонентах", "d) useEffect синхронен по умолчанию"],
        "answer": "d) useEffect синхронен по умолчанию"
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
