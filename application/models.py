from application import db

class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rus = db.Column(db.Text)
    eng = db.Column(db.Text)
    level = db.Column(db.Integer)
    difficulty = db.Column(db.Integer)

    def __init__(self, rus, eng, level, difficulty):
        self.rus = rus
        self.eng = eng
        self.level = level
        self.difficulty = difficulty

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sber_id = db.Column(db.Text)
    level = db.Column(db.Integer)
    difficulty = db.Column(db.Integer)

    def __init__(self, sber_id, level, difficulty):
        self.sber_id = sber_id
        self.level = level
        self.difficulty = difficulty
