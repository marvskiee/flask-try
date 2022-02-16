from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '7a56c15eee8dffdc716af8121622ec22'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://yjqzdocqtuccus:3985352e5147c9f3711b1da4e24946f36f44bbf30f73f097b0c73acfd96d6006@ec2-18-208-97-23.compute-1.amazonaws.com:5432/d3bk4hevkhhbu7'

db = SQLAlchemy(app)

from app import routes
