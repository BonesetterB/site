from bs4 import BeautifulSoup
import requests

base_url='https://opencritic.com/'

url = "https://opencritic.com/browse/pc"

def get_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    list_games= soup.find('div', class_='desktop-game-display').find_all('a')
    return list_games

def get_game(url):
    game = requests.get(f'{base_url}{url}')
    soup = BeautifulSoup(game.content, "lxml")
    companies= soup.find('div', class_='container').find('div', class_='companies').find_all('span')

    date=soup.find('div', class_='container').find('div')

    img= soup.find('div', class_='header-image-container').find('picture').find('img')
    name_game=soup.find('div', class_='container').find('div', class_='card-body').find('h1',class_='game-name')
    list_game={}
    return list_game

x=get_page(url)

for i in x:
    game=get_game(i['href'])
