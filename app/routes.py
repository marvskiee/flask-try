from os import defpath

from flask import render_template,url_for
from werkzeug.utils import redirect
from app import app
from app.models import *
from app import db

import json

@app.route('/')
def index():
    if Songs.query.count() < 1:
        with open('phchords.json') as f:
            data = json.load(f)
        for d in data:
            song = Songs(mode=d['mode'], artist=d['artist'], chords=d['chords'], title=d['title'],lyrics=d['lyrics'])    
            db.session.add(song)
        db.session.commit()
        
    return render_template('index.html')

@app.route('/search/<string:song>',methods=['POST','GET'])
def song(song):
    result = Songs.query.filter(Songs.title.like(f'%{song}%')).all()
    return render_template('search.html',result=result)
@app.route('/request')
def show():
    result = Request.query.all()
    return render_template('request.html',result=result)

@app.route('/request/<string:data>/<string:status>',methods=['POST','GET'])
def request(data,status):
    req = Request(data=data,status=status)
    db.session.add(req)
    db.session.commit()
    result = Request.query.all()
    return redirect('/request')