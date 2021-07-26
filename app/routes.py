from os import defpath

from flask import render_template,url_for,request
from werkzeug.utils import redirect
from app import app
from app.models import *
from app import db

import requests
import json

@app.route('/')
def index():
    return 'home'

@app.route('/webhook', methods=['POST','GET'])
def webhoook():
    status=mode=token=challenge = ''
    VERIFY_TOKEN = '7a56c15eee8dffdc716af8121622ec22'
    if request.method == 'POST':
        if request.get_json().get('object')=='page':
            entry = request.get_json().get('entry')
            for e in entry:
                print(e['messaging'][0])
            return 'EVENT_RECEIVED'
        else:
            return '404'


    if 'hub.mode' in request.args:
        mode = request.args.get('hub.mode')
        print(mode)
    if 'hub.verify_token' in request.args:
        token = request.args.get('hub.verify_token')
        print(token)
    if 'hub.challenge' in request.args:
        challenge = request.args.get('hub.challenges')
        print(challenge)
    
    if mode and token:
        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return 'WEBHOOK VERIFIED'
    else:
        return 'TOKENS DO NOT MATCH'