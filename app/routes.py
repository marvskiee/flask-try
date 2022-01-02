from os import defpath
# scrape
from bs4 import BeautifulSoup
import requests
from markupsafe import escape,Markup
from flask import render_template,url_for
from werkzeug.utils import redirect
from app import app
from app.models import *
from app import db

import json

@app.route('/')
def index():
    with open('app/test.html','r') as html_file:
        content = html_file.read()
        soup = BeautifulSoup(content,'lxml')
        target_button = soup.find_all('button')
        for t in target_button:
            print(t.text)
    return render_template('index.html')

@app.route('/test')
def test():
    html_text = requests.get('https://chia-anime.su/').text
    soup = BeautifulSoup(html_text, 'lxml')
    category = soup.find_all('div', class_='bixbox')
    latest_card = category[0].find_all('article', class_='bs')
    recommended_card = category[1].find_all('article', class_='bs')
    recommended = list_scraper(recommended_card)
    latest = list_scraper(latest_card)
    print(json.dumps(latest,indent=4,sort_keys=True))

    return {"latest":latest,"recommended": recommended}
@app.route('/anime/<pathname>')
def anime(pathname):
    html_text = requests.get(f'https://chia-anime.su/{escape(pathname)}').text
    soup = BeautifulSoup(html_text, 'lxml')
    video = soup.find('div',class_='video-content')
    print(video)
    return render_template('video.html',video=Markup(video))


def list_scraper(raw_data):
    temp = []
    for card in raw_data:
        link = card.find('a', href=True)['href'].split('/')[-1]
        name = card.find('div',class_='tt').text
        episode = card.find('span', class_='epx').text
        filter = card.find('span', class_='sb Sub').text
        image = card.img['src']
        temp.append({
            "link": link,
            "name": name,
            "epidsode":episode,
            "filter": filter,
            "image": image
        })
    return temp


