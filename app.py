from flask import Flask
from flask import jsonify, render_template, make_response

from utils import test_mybook


app = Flask(__name__)


#  рендерит стартовую страницу
@app.route('/', methods=['GET'])
def main():
    response = test_mybook()
    return render_template('index.html', title='Book list', response=response), 200


if __name__ == '__main__':
    app.run()
