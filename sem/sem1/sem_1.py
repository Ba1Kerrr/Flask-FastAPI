from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('user.html')


@app.route('/about/')
def about():
    return 'about!'


@app.route('/contact/')
def contact():
    return 'contact'


@app.route('/<int:num1>/<int:num2>')
def summ_url(num1, num2):
    return str(num1 + num2)


@app.route('/<stroka>/')
def len_url(stroka):
    return str(len(stroka))


@app.route('/get-html/')
def get_html():
    return ('''
        <h1>Моя первая HTML страница</h1>
        <p>Привет, мир!</p>
      ''')


@app.route('/students/')
def get_students():
    students = [
        {"first_name": "denis", "last_name": "davydov", "age": 36},
        {"first_name": "liza", "last_name": "davydova", "age": 33},
        {"first_name": "danya", "last_name": "davydov", "age": 14},
        {"first_name": "artem", "last_name": "davydov", "age": 6}
    ]
    return render_template('students.html', students=students)


@app.route('/news/')
def get_news():
    news = [
        {"title": "TITLE", "date": "15.05.2024", "description": "DESCRIPTION"},
        {"title": "TITLE", "date": "15.05.2024", "description": "DESCRIPTION"},
        {"title": "TITLE", "date": "15.05.2024", "description": "DESCRIPTION"},
        {"title": "TITLE", "date": "15.05.2024", "description": "DESCRIPTION"}
    ]
    return render_template('news.html', news=news)


if __name__ == '__main__':
    app.run(debug=True)
