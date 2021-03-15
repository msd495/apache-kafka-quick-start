from time import sleep

import requests
from bs4 import BeautifulSoup
from kafka import KafkaProducer

def fetch_raw(recipe_url,headers):
    html = None
    print('Processing..{}'.format(recipe_url))
    try:
        r = requests.get(recipe_url, headers=headers)
        if r.status_code == 200:
            html = r.text
    except Exception as ex:
        print('Exception while accessing raw html')
        print(str(ex))
    finally:
        return html.strip()


def get_recipes(headers):
    recipies = []
    salad_url = 'https://www.allrecipes.com/recipes/96/salad/'
    url = 'https://www.allrecipes.com/recipes/96/salad/'
    print('Accessing list')

    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            html = r.text
            #soup = BeautifulSoup(html, 'lxml')
            #links = soup.select('.submenu-link heading-menu a')
            idx = 0
            links = [
                {
                    "@type": "ListItem",
                    "position": 1,
                    "url": "https://www.allrecipes.com/recipe/213165/pear-and-pomegranate-salad/"
                },
                {
                    "@type": "ListItem",
                    "position": 2,
                    "url": "https://www.allrecipes.com/recipe/43781/tropical-turkey-salad/"
                },
                {
                    "@type": "ListItem",
                    "position": 3,
                    "url": "https://www.allrecipes.com/recipe/14472/fennel-and-watercress-salad/"
                }
            ]
            for link in links:
                sleep(2)
                #recipe = fetch_raw(link["url"],headers)
                recipies.append(link)
                idx += 1
    except Exception as ex:
        print('Exception in get_recipes')
        print(str(ex))
    finally:
        return recipies