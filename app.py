from flask import Flask, request

app = Flask(__name__)


@app.route('/hello', methods=['POST'])
def hello():
    name = request.form.get('name')

    if name:
        return f'Hello {name}!'
    else:
        return 'Hello weirdo!'