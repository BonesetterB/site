from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
epic='https://store.epicgames.com/en-US/p/'
viki='https://en.wikipedia.org/wiki/'

game='The Evil Within 2'
game_for_vici=game.replace(' ', '_')
game_for_epic=game.lower().replace(' ', '-')





def get_viki(url,game):
    print(f"{url}{game}")
    page = requests.get(f"{url}{game}")
    soup = BeautifulSoup(page.content, "lxml")
    desk= soup.find('div', class_='mw-content-container').find('div', class_='mw-parser-output').find('h2').find_all_previous('p')
    desk_reversed = list(reversed(desk))
    return desk_reversed

def get_epic(url,game):
    print(f"{url}{game}")
    driver = webdriver.Chrome()
    x=driver.get(f'{url}{game}')
    mm=driver.page_source
    time.sleep(360)
    # page = requests.get(f"{url}{game}")
    # soup = BeautifulSoup(page.content, "lxml")
    # desk= soup
    return mm

# print("viki :  \n", get_viki(viki,game_for_vici))

print("Eppicc :  \n", get_epic(epic,game_for_epic))