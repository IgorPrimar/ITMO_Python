# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:55:00 2024

@author: krivoshein
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_articles_from_page(page_number):
    url = f'https://lifehacker.ru/category/tehnologii/page/{page_number}/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []
    
    for article in soup.find_all(class_='post'):
        title = article.find(class_='post-title').get_text(strip=True)
        link = article.find('a')['href']
        articles.append((title, link))
    return articles

all_articles = []
for i in range(1, 11):
    all_articles.extend(get_articles_from_page(i))
    
unique_links = set(link for _, link in all_articles)

def get_article_content(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find(class_='post-content').get_text(strip=True)
    return content

data = []
for title, link in all_articles:
    content = get_article_content(link)
    data.append({'title': title, 'content': content})

df = pd.DataFrame(data)
print(df)
