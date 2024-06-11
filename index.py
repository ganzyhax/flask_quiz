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
        "options": ["a) useEffect", "b) useReducer",  "c) useContext",  "d) useState"],
        "answer": "d) useState"
    },
    {
        "question": '''Какой из следующих примеров правильно выполняет GET-запрос к серверу с использованием useEffect?

javascript
Копировать код
import React, { useState, useEffect } from 'react';

function DataFetcher() {
    const [data, setData] = useState(null);
useEffect(() => {
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

export default DataFetcher;''',
        "options": ["a) useEffect без пустого массива", "b) useEffect с пустым массивом", "c) useEffect с объектом", "d) useEffect с функцией"],
        "answer": "b) useEffect с пустым массивом"
    },
    {
        "question": '''Как вызвать функцию только один раз после монтирования компонента с использованием useEffect?

javascript
Копировать код
useEffect(() => {
    // Ваш код здесь
}, []);''',
        "options": ["a) Передать пустой массив вторым аргументом в useEffect", "b) Не передавать второй аргумент в useEffect", "c) Передать null вторым аргументом в useEffect", "d) Передать true вторым аргументом в useEffect"],
        "answer": "a) Передать пустой массив вторым аргументом в useEffect"
    },
    
    {
        "question": "Какой hook используется для выполнения побочных эффектов в функциональных компонентах?",
        "options": ["a) useState", "b) useReducer", "c) useEffect", "d) useContext"],
        "answer": "c) useEffect"
    },
    
    {
        "question": "Какой hook используется для управления состоянием в функциональных компонентах?",
        "options": ["a) useEffect", "b) useReducer", "c) useContext", "d) useState"],
        "answer": "d) useState"
    },

    
    {
        "question": "Какой тип данных возвращает функция range() в Python 3?",
        "options": ["a) useEffect вызывается до рендера компонента", "b) useEffect вызывается после каждого рендера компонента", "c) useEffect нельзя использовать в функциональных компонентах", "d) useEffect синхронен по умолчанию"],
        "answer": "d) useEffect синхронен по умолчанию"
    },
    {
        "question": '''Что выведет следующий код?,
        python
        Копировать код
        print(type({}))''',
        "options": ["a) <class 'list'>", "b) <class 'set'>", "c) <class 'dict'>", "d) <class 'tuple'>"],
        "answer": "c) <class 'dict'>"
    },
    {
        "question": '''Какой результат выполнения следующего list comprehension?, python
Копировать код
[x**2 for x in range(5)]''',
        "options": ["a) [1, 4, 9, 16, 25]","b) [0, 1, 4, 9, 16]", "c) [0, 1, 4, 9, 16, 25]", "d) [1, 4, 9, 16]"],
        "answer": "b) [0, 1, 4, 9, 16]"
    },
    "question": '''Напишите функцию, которая принимает список чисел и возвращает новый список, содержащий только четные числа из исходного списка.
    python
Копировать код
def filter_even_numbers(numbers):
# Ваш код здесь''',
        "options": ["a) return [x for x in numbers if x % 2 == 0]", "b) return [x if x % 2 == 0 for x in numbers]", "c) return [x in numbers if x % 2 == 0]", "d) return [numbers for x in numbers if x % 2 == 0]"],
        "answer": "a) return [x for x in numbers if x % 2 == 0]"
    },
    {
        "question": '''Какой результат выполнения следующего кода?

python
Копировать код
x = [1, 2, 3]
y = x
y.append(4)
print(x)''',
        "options": ["a) [1, 2, 3]", "b) [1, 2, 3, 4]", "c) [1, 2, 4]", "d) Ошибка времени выполнения (runtime error)"],
        "answer": "b) [1, 2, 3, 4]"
    },
    {
        "question": "Какое время выполнения (O(n)) у операции добавления элемента в конец списка (list) в Python?",
        "options": ["a) O(1)", "b) O(n)", "c) O(log n)", "d) O(n^2)"],
        "answer": "a) O(1)"
    },
    {
        "question": "Какое время выполнения (O(n)) у операции поиска элемента в хэш-таблице (dict) в среднем случае в Python?",
        "options": ["a) O(1)", "b) O(n)", "c) O(log n)", "d) O(n^2)"],
        "answer": "a) O(1)"
    },
    {
        "question": '''Напишите функцию, которая принимает строку и возвращает словарь, где ключи — это символы строки, а значения — количество их вхождений.

def char_count(s):
    # Ваш код здесь",
        "options": ["a) return {char: s.count(char) for char in s}", "b) return {char: count for char, count in s}", "c) return {s.count(char): char for char in s}", "d) return {char: s.count(char) for char in set(s)}"],
        "answer": "d) return {char: s.count(char) for char in set(s)}"
    },
    {
        "question": '''Какое значение будет у переменной x после выполнения следующего кода?

python
Копировать код
x = 5
x *= 3''',
        "options": ["a) 8", "b) 15", "c) 5:, "d) 2"],
        "answer": "b) 15"
    },
    {
        "question": "Какое ключевое слово используется для обработки исключений в Python?",
        "options": ["a) try", "b) catch", "c) except", "d) finally"],
        "answer": "c) except"
    },
    {
        "question": "Какое ключевое слово используется для обработки исключений в Python?",
        "options": ["a) try", "b) catch", "c) except", "d) finally"],
        "answer": "c) except"
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
