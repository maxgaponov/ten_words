import json
import logging
from flask import request
from application import app, db, user_data
from application.models import Word, User

@app.route('/new_game', methods=['GET', 'POST'])
def new_game():
    global user_data

    req_data = request.get_json()
    id = req_data['id']
    
    user = User.query.filter_by(sber_id=id).first()
    res = {}
    if user is None:
        db.session.add(User(id, 0))
        db.session.commit()
        res = {'level': 0}
    else:
        res = {'level': user.level}

    user_data[id] = {
        'word_list': list(map(lambda word: (word.rus, word.eng), Word.query.filter_by(level=res['level'], difficulty=2).all())),
        'cur_word': 0,
        'testing_phase': False,
    }

    response = app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/next_word', methods=['GET', 'POST'])
def next_word():
    global user_data

    req_data = request.get_json()
    id = req_data['id']
    wa = req_data['wa']

    res = {}

    if user_data[id]['testing_phase']:
        pass
    else:
        idx = user_data[id]['cur_word']
        cur_word = user_data[id]['word_list'][idx]
        res = {'word_rus': cur_word[0], 'word_eng': cur_word[1], 'end': False}
        user_data[id]['cur_word'] += 1
    
    response = app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json'
    )
    return response
