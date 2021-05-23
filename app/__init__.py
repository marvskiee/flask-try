from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '7a56c15eee8dffdc716af8121622ec22'
app.config['SQLALCHEMY_TRACK_MODIDFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://monsywklmjvnbw:9da65ca06e0f8617868ccfb29d4c6e7939dac629227f92f3df9971b4d31c85c7@ec2-18-215-111-67.compute-1.amazonaws.com:5432/dcu6d7n401lbtt'

db = SQLAlchemy(app)

from app import routes