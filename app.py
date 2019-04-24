from flask import Flask
from flask import jsonify, render_template, make_response


app = Flask(__name__)


#  рендерит стартовую страницу
@app.route('/', methods=['GET'])
def main():
    return render_template('index.html', title='Book list',), 200


if __name__ == '__main__':
    app.run()
