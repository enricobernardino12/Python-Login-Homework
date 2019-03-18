from flask import Flask, render_template,request, url_for, redirect
app = Flask(__name__)

@app.route('/', methods=['GET'])
def login_form():
    return render_template('login_form.html')

@app.route('/success')
def success_login():
    return render_template('success.html')

@app.route('/', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']
    error = None
    if email != 'test@flask.app' or password != 'password123':
        error = 'Invalid Credentials. Please try again.'
    else:
        return redirect(url_for('success_login'))
    return render_template('login_form.html', error=error)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
