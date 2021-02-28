import json
from flask import request
from application import app, db, user_data
from application.models import Word, User

@app.route('/new_game', methods=['GET', 'POST'])
def new_game():
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
    response = app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/next_word', methods=['GET', 'POST'])
def next_word():
    req_data = request.get_json()
    id = req_data['id']
    wa = req_data['wa']
    res = {'word_rus': 'Собака', 'word_eng': 'Dog', 'end': False}
    response = app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json'
    )
    return response
