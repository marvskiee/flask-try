from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '7a56c15eee8dffdc716af8121622ec22'
app.config['SQLALCHEMY_TRACK_MODIDFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://fpqlltxsardwje:94c0509e0017b3fd077113aef07e18b76411b9361abde2a906954577f876a62a@ec2-44-194-113-156.compute-1.amazonaws.com:5432/d896jjv31g4ma1'

db = SQLAlchemy(app)

from app import routes
