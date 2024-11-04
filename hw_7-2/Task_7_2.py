# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 22:21:55 2024

@author: krivoshein
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'https://lifehacker.ru'
response = requests.get('https://lifehacker.ru/topics/technology/')
soup = BeautifulSoup(response.text, 'lxml')
raw_items = soup.find_all('div', class_='lh-small-article-card__title')
raw_links = soup.find_all('a', class_='lh-small-article-card__link')

# Извлекаем текст заголовков и ссылок
titles = [item.get_text(strip=True) for item in raw_items]
links = [base_url + item.get('href') for item in raw_links if item.get('href')]

# Получаем содержимое статей
article_data = []
for link in links[:10]:
    article_response = requests.get(link)
    article_soup = BeautifulSoup(article_response.text, 'lxml')
    content = article_soup.find('div', class_='article-card single-article-card')
    article_text = content.get_text(strip=True) if content else 'Нет содержимого'
    article_data.append(article_text)

df = pd.DataFrame({
    'Title': titles[:10],
    'Link': links[:10],
    'Content': article_data[:10]
})

pd.set_option('display.max_colwidth', 400)
print(df.head(10))
df.to_excel('lifehacker_articles.xlsx', index=False)