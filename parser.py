from bs4 import BeautifulSoup
import requests

base_url='https://opencritic.com/'

url = "/browse/pc"

def get_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "lxml")
    list_games= soup.find('div', class_='desktop-game-display').find_all('a')
    return list_games

def get_game(url):
    game = requests.get(f'{base_url}{url}')
    soup = BeautifulSoup(game.content, "lxml")
    img=None
    date=soup.find('app-page-container-right-nav').find('div', class_='container').find('div', class_='platforms').text
    companies = [span.text for span in soup.find('app-page-container-right-nav').find('div', class_='container').find('div', class_='companies').find_all('span')]
    platforms = [span.text for span in soup.find('app-page-container-right-nav').find('div', class_='container').find('div', class_='platforms').find_all('span')]

    img_sel=soup.find('div', class_='header-image-container')
    if img_sel:
        img_tag= soup.find('div', class_='header-image-container').find('picture').find('img')
        img = img_tag.get('src')
    name_game=soup.find('app-page-container-right-nav').find('div', class_='container').find('div', class_='card-body').find('h1',class_='mb-0').text

    list_game={"img":img,
               'name':name_game,
               'companies':companies,
               'platforms':platforms,
               'date':date}
    return list_game

for i in range(2):
    url_x=f'{base_url}{url}'
    x=get_page(url_x)
    for i in x:
        print(i.text)
        game=get_game(i['href'])
        print(game)
    page = requests.get(url_x)
    soup = BeautifulSoup(page.content, "lxml")
    url= soup.find('app-page-container-right-nav').find('div', class_='container').find('div', class_='row no-gutters page-row-bottom py-2 mt-1').find('a',rel='next')["href"]

    if url == None:
        break
