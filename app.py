from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    # return index.html
    return '<h1>Hello, World!</h1>'

@app.route('/login')
def login():
    # return file_list.html
    if request.args.get('password') == '1234':
        return '<h1>After Login</h1>'
    else:
        return '<h1>Login Failed!</h1>'