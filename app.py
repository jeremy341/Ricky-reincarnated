from flask import Flask, request
import random 

app = Flask(__name__)


@app.route('/hello', methods=['POST'])
def hello():
    name = request.form.get('name')

    if name:
        return f'Hello {name}!'
    else:
        return 'Hello weirdo!'


@app.route('/roll', methods=['POST'])
def roll():
    roll = request.form.get('roll')

    if roll:
        number = int(roll)
    else:
        number = 6

    random_number = random.randint(1, number)
    return f'You rolled a {random_number}!'