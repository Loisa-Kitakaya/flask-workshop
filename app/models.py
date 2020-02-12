from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),unique=True,nullable=False)
    password = db.Column(db.Text,nullable=False)

    def set_password(self,p):
        self.password = generate_password_hash(p)

    def check_password(self,p):
        return check_password_hash(self.password,p)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Device(db.Model):
    __tablename__ = "devices"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255),nullable=False)
    state = db.Column(db.Boolean)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    user = db.relationship("User",backref=db.backref("devices",lazy=True))
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

