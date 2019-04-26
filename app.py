from flask import Flask
from flask import jsonify, render_template, request, redirect, url_for, session

from utils import mybook


app = Flask(__name__)

app.secret_key = 'BOOK_007'


#  рендерит стартовую страницу
@app.route('/', methods=['GET'])
def main():
    # print(session.get('user_email'), session.get('user_password'))
    user_email = session.get('user_email')
    user_password = session.get('user_password')
    response = mybook(user_email, user_password)
    return render_template('index.html', title='Book list', response=response), 200


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        session['user_email'] = request.form['email']
        session['user_password'] = request.form['password']
        return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug=True)
