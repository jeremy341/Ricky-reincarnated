from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'



@app.route('/hello', methods=['POST'])
def hello():
    return 'Hello Iam ricky!'