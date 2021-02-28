import json
from flask import request
from application import app, db, user_data
from application.models import Word, User

@app.route('/new_game', methods=['GET', 'POST'])
def new_game():
    id = request.values['id']
    user = User.query.filter_by(sber_id=id).first()
    if user is None:
        db.session.add(User(id, 0))
        db.session.commit()
        return json.dumps({'level': 0})
    else:
        return json.dumps({'level': user.level})

@app.route('/next_word', methods=['GET', 'POST'])
def next_word():
    id = request.values['id']
    wa = request.values['wa']
    return json.dumps({'word_rus': 'Собака', 'word_eng': 'Dog', 'end': False})
