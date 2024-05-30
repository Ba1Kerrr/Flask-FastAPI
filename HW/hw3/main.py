from flask import Flask, request, render_template
from flask_wtf.csrf import CSRFProtect
from form_register import RegistrationForm
from model_user import db, User

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///mydatabase.db'
db.init_app(app)

app.config['SECRET_KEY'] = "4247276b47775a091b5d58dc0a7fa79f5f318aaf637d7cb583f58c09ee947743"
csrf = CSRFProtect(app)


@app.route("/")
def index():
    return render_template("base.html")


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(firstname=firstname, lastname=lastname, email=email).first()
        if user:
            return 'Такой пользователь уже есть!'
        else:
            new_user = User(firstname=firstname, lastname=lastname, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return 'Пользователь успешно зарегистрирован'
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
