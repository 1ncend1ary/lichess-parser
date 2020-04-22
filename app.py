from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os
from checker import check
import secret

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(12)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')


@app.route('/check', methods=['POST'])
def check_arguments():
    tid = request.form['tid']
    games = int(request.form['games'])
    moves = int(request.form['moves'])
    title = request.form['title']
    names = check(tid, games, moves, title)
    flash(names)
    return redirect(url_for('home'))


@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == secret.password and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('Incorrect credentials!')
    return redirect(url_for('home'))


if __name__ == "__main__":
    # app.secret_key =
    app.run(debug=False, host='0.0.0.0', port=5000)
