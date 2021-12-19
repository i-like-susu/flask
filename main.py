from flask import Flask

__author__ = 'xiaode'

app = Flask(__name__)
app.config.from_pyfile('config/base_setting.py')


@app.route('/hello')
def hello():
    return 'hello flask'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
