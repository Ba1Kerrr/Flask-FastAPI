from flask import Flask, request, render_template, redirect, url_for, flash, make_response

app = Flask(__name__)
app.secret_key = b'erf45efr4s5ef54es35f4rs3e4'


@app.route("/")
@app.route("/user/")
def user():
    return render_template("user.html",
                           title="user",
                           name=request.cookies.get("name"),
                           email=request.cookies.get("email"))


@app.route("/form/", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['email']:
            flash('Необходимо ввести данные!', 'danger')
            return redirect(url_for('form'))
        name = request.form.get('name'),
        email = request.form.get('email')
        response = redirect(url_for("user", name=name, email=email))
        response.set_cookie(key="user", value=f'{name}-{email}')
        return response
    return render_template("form.html")


@app.route('/logout/')
def logout():
    response = redirect(url_for('form'))
    response.delete_cookie("user")
    return response


if __name__ == '__main__':
    app.run(debug=True)
