from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_hackernews_titles():
    resp = requests.get('https://news.ycombinator.com/')
    soup = BeautifulSoup(resp.text)
    links = soup.find_all('a', class_='storylink')
    titles = []
    for link in links:
        titles.append((link.string, link['href']))
    return titles

@app.route('/')
def hellohello():
    titles = get_hackernews_titles()
    return render_template('home.html', titles=titles, homePageTitle='Stanlee')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

