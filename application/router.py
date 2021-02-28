import json
from flask import request
from application import app, db, user_data
from application.models import Word, User

@app.route('/new_game', methods=['GET', 'POST'])
def new_game():
    try:
        id = request.form['id']
        user = User.query.filter_by(sber_id=id).first()
        if user is None:
            db.session.add(User(id, 0))
            db.session.commit()
            return json.dumps({'level': 0})
        else:
            return json.dumps({'level': user.level})
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
