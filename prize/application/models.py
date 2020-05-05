from application import db, login_manager
from flask_login import UserMixin



@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))


class Prizes(db.Model):
    prize_id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(15), nullable=False)
    prize = db.Column(db.String(4), nullable=False)
    id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  

    def __repr__(self):
        return ''.join([
            'Code: ', self.code, ' ', '\r\n',
            'Prize: ', self.prize, '\r\n'
            ])

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    player = db.relationship('Prizes', backref='author', lazy=True)

    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name
        ])