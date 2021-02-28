import json
import random
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
        'word_list': list(map(lambda word: (word.rus, word.eng), Word.query.filter_by(level=res['level'], difficulty=2).limit(5))),
        'cur_word': 0,
        'testing_phase': False,
    }

    # logging.error(user_data)

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

    # logging.error(user_data)

    if user_data[id]['testing_phase']:
        if not wa and user_data[id]['cur_word'] == len(user_data[id]['word_list']):
            res = {'word_rus': '', 'word_eng': '', 'end': True}
            user = User.query.filter_by(sber_id=id).first()
            user.level += 1
            db.session.commit()
        elif user_data[id]['cur_word'] == -1:
            res = {'word_rus': '', 'word_eng': '', 'end': True}
            user_data[id]['cur_word'] += 1
        else:
            if wa:
                user_data[id]['cur_word'] -= 1
                idx = user_data[id]['cur_word']
                wa_word = user_data[id]['word_list'].pop(idx)
                user_data[id]['word_list'].append(wa_word)
                cur_word = user_data[id]['word_list'][idx]
                res = {'word_rus': cur_word[0], 'word_eng': cur_word[1], 'end': False}
                user_data[id]['cur_word'] += 1
            else:
                idx = user_data[id]['cur_word']
                cur_word = user_data[id]['word_list'][idx]
                res = {'word_rus': cur_word[0], 'word_eng': cur_word[1], 'end': False}
                user_data[id]['cur_word'] += 1
    else:
        idx = user_data[id]['cur_word']
        cur_word = user_data[id]['word_list'][idx]
        res = {'word_rus': cur_word[0], 'word_eng': cur_word[1], 'end': False}
        user_data[id]['cur_word'] += 1
        if user_data[id]['cur_word'] == len(user_data[id]['word_list']):
            user_data[id]['cur_word'] = -1
            user_data[id]['testing_phase'] = True
            random.shuffle(user_data[id]['word_list'])
    
    response = app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json'
    )
    return response
