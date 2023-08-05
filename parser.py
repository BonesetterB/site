from bs4 import BeautifulSoup
import requests
from datebase.Modules import Game
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

base_url='https://opencritic.com/'

url = "/browse/pc?page=536"

db_path = 'sqlite:///D:/python/site/instance/database.db'


engine = create_engine(db_path)


Session = sessionmaker(bind=engine)

def get_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    list_games= soup.find('div', class_='desktop-game-display').find_all('a')
    return list_games

def get_game(url):
    game = requests.get(f'{base_url}{url}')
    soup = BeautifulSoup(game.content, "lxml")
    img_url=None
    dates=soup.find('app-page-container-right-nav').find('div', class_='container').find('div', class_='platforms').text
    companiess = [span.text for span in soup.find('app-page-container-right-nav').find('div', class_='container').find('div', class_='companies').find_all('span')]
    platformss = [span.text for span in soup.find('app-page-container-right-nav').find('div', class_='container').find('div', class_='platforms').find_all('span')]

    img_sel=soup.find('div', class_='header-image-container')
    if img_sel :
        img_tag= soup.find('div', class_='header-image-container').find('picture').find('img')
        img_url = img_tag.get('src')
    name_game=soup.find('app-page-container-right-nav').find('div', class_='container').find('div', class_='card-body').find('h1',class_='mb-0').text

    new_game=Game(img=img_url, name=name_game,companies=companiess,platforms=platformss,date=dates)
    return new_game

def save_base(game):
    session = Session()

    try:
        session.add(game)

        session.commit()

        print("Game збережено успішно.")
    except Exception as e:
        session.rollback()

        print("Помилка збереження: ", e)
    finally:
        session.close()

while True:
    url_x=f'{base_url}{url}'
    x=get_page(url_x)
    for i in x:
        print(i.text)
        game=get_game(i['href'])
        save_base(game)
    page = requests.get(url_x)
    soup = BeautifulSoup(page.content, "lxml")
    try:
        url= soup.find('app-page-container-right-nav').find('div', class_='container').find('div', class_='row no-gutters page-row-bottom py-2 mt-1').find('a',rel='next')["href"]
    except TypeError:
        break


