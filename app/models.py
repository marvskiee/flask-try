from enum import unique
from app import db

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(50),unique=True, nullable=False)
    status =  db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"{self.id}, {self.data}, {self.status}"

class Songs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    artist =  db.Column(db.String(50), nullable=False)
    lyrics =  db.Column(db.Text, nullable=False)
    mode =  db.Column(db.String(10), nullable=False)
    chords =  db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"{self.id}, {self.title}, {self.artist}, {self.lyrics}, {self.mode}, {self.chords}"