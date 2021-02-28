import json
from flask import request
from application import app, user_data
from application.models import Word, User

@app.route('/new_game', methods=['GET', 'POST'])
def new_game():
    try:
        id = request.form['id']
        return json.dumps({'level': 0})
    except KeyError:
        return json.dumps({'level': 0})

@app.route('/next_word', methods=['GET', 'POST'])
def next_word():
    try:
        id = request.form['id']
        wa = request.form['wa']
        return json.dumps({'word_rus': 'Собака', 'word_eng': 'Dog', 'end': False})
    except KeyError:
        return json.dumps({'word_rus': 'Собака', 'word_eng': 'Dog', 'end': False})
