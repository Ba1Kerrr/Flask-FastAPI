import random

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/cloth/')
def get_cloth():
    description = ('Lorem ipsum dolor, sit amet consectetur adipisicing elit. '
                   'Quasi eligendi culpa pariatur, maiores aperiam minus excepturi reprehenderit numquam unde cumque, '
                   'asperiores placeat, molestias quod aliquam enim consequatur nesciunt. Sit assumenda temporibus et'
                   ' impedit!')

    cloth = [
        {"title": "Брюки", "description": description, "price": random.randint(10,100)},
        {"title": "Верхняя одежда", "description": description, "price": random.randint(10,100)},
        {"title": "Джемперы, водолазки и кардиганы", "description": description, "price": random.randint(10,100)},
        {"title": "Джинсы", "description": description, "price": random.randint(10,100)},
        {"title": "Комбинезоны и полукомбинезоны", "description": description, "price": random.randint(10,100)},
        {"title": "Костюмы", "description": description , "price": random.randint(10,100)}
    ]
    return render_template('cloth.html', cloth=cloth)

@app.route('/shoes/')
def get_shoes():
    description = ('Lorem ipsum dolor, sit amet consectetur adipisicing elit. '
                   'Quasi eligendi culpa pariatur, maiores aperiam minus excepturi reprehenderit numquam unde cumque, '
                   'asperiores placeat, molestias quod aliquam enim consequatur nesciunt. Sit assumenda temporibus et'
                   ' impedit!')

    shoes = [
        {"title": "Ботинки и полуботинки", "description": description, "price": random.randint(10,100)},
        {"title": "Кеды и кроссовки", "description": description, "price": random.randint(10,100)},
        {"title": "Мокасины и топсайдеры, водолазки и кардиганы", "description": description, "price": random.randint(10,100)},
        {"title": "Сапоги и унты", "description": description, "price": random.randint(10,100)},
        {"title": "Тапочки", "description": description, "price": random.randint(10,100)},
        {"title": "Туфли и лоферы", "description": description , "price": random.randint(10,100)},
        {"title": "Шлепанцы и аквасоки", "description": description, "price": random.randint(10,100)},

    ]
    return render_template('shoes.html', shoes=shoes)

@app.route('/jackets/')
def get_jackets():
    description = ('Lorem ipsum dolor, sit amet consectetur adipisicing elit. '
                   'Quasi eligendi culpa pariatur, maiores aperiam minus excepturi reprehenderit numquam unde cumque, '
                   'asperiores placeat, molestias quod aliquam enim consequatur nesciunt. Sit assumenda temporibus et'
                   ' impedit!')

    jackets = [
        {"title": "Ветровки", "description": description, "price": random.randint(10,100)},
        {"title": "Бомберы и лётные куртки", "description": description, "price": random.randint(10,100)},
        {"title": "Мотоциклетные куртки", "description": description, "price": random.randint(10,100)},
        {"title": "Полевые куртки", "description": description, "price": random.randint(10,100)},
        {"title": "Стёганые куртки", "description": description, "price": random.randint(10,100)}

    ]
    return render_template('jackets.html', jackets=jackets)

if __name__ == '__main__':
    app.run(debug=True)

