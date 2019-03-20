from flask import Flask, render_template, session, redirect, url_for, escape, request, make_response
app = Flask(__name__)

app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

@app.route('/', methods=['GET'])
def login_form():
    return render_template('login_form.html')

@app.route('/my-profile')
def success_login():
    loginError = "Please login first"
    relay= None
    if 'username' in session:
        count = request.cookies.get('count')
        if count == '1':
            relay = 'Welcome Back'
        else:
            relay ='Welcome'

        return render_template('success.html', username=session["username"], password=session["password"], relay= relay)
    return render_template('login_form.html', loginError=loginError)

@app.route('/', methods=['POST'])
def login_user():
    username = request.form['username']
    password = request.form['password']
    error = None
    if username != 'test@flask.app' or password != 'password123':
        error = 'Invalid Credentials. Please try again.'
    else:
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return redirect(url_for('success_login'))
    return render_template('login_form.html', error=error)

@app.route('/logout')
def logout():
    response = redirect(url_for("login_user"))
    response.set_cookie('count', '1')
    # remove the username from the session if it's there
    session.pop('username', None)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
