# -*- coding: utf-8 -*-
import requests
import pandas as pd
url = "https://www.anapioficeandfire.com/api/houses"

# Получение данных"
house_list = requests.get(url)
df_house = pd.DataFrame(house_list.json())
print("Все данные:\n",df_house)

# Проверка, есть ли дома с регионом "The Westerlands"
response = requests.get(url)
if response.status_code == 200:
    df_houses = pd.DataFrame(response.json())
    if 'region' in df_houses.columns:
        idx = df_houses[df_houses['region'] == 'The Westerlands'].values[0]
        print("Дома в Westerlands:\n", idx)
    else:
        print("В данных нет колонки 'region'.")
else:
    print("Ошибка при получении данных.")

# Проверка, есть ли дома с регионом "The Westerlands с девизом"
params = {'hasTitles': True}
response = requests.get(url, params=params)
if response.status_code == 200:
    df_houses = pd.DataFrame(response.json())
    if 'region' in df_houses.columns:
        idx = df_houses[df_houses['region'] == 'The Westerlands']
        print("Дома в Westerlands c девизом:\n", idx)
    else:
        print("В данных нет колонки 'region'.")
else:
    print("Ошибка при получении данных.")