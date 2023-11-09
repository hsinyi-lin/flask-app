from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


@app.route('/num')
def num_page():
    num = 1
    return str(num)


@app.route('/detail')
def detail_page():
    return 'Detail Page'

@app.route('/welcome')
def welcome_page():
    return 'Welcome Page'

if __name__ == '__main__':
    app.run()