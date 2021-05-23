from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '7a56c15eee8dffdc716af8121622ec22'
app.config['SQLALCHEMY_TRACK_MODIDFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://azupiyqwdemjrw:305b9ddad54d07868e1626697d5c8ad56d00965f7560bfb43f1457c5913cd06e@ec2-52-22-161-59.compute-1.amazonaws.com:5432/dc0cq7olc0ea15'

db = SQLAlchemy(app)

from app import routes