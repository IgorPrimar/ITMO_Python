# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:24:47 2024

@author: krivoshein
"""

import pandas as pd
import bottleneck as bn

# Чтение данных из файла
data = pd.read_csv('train.csv')

# 1. Средний возраст пассажиров и его стандартное отклонение с помощью bottleneck
average_age = bn.nanmean(data['Age'])
std_age = bn.nanstd(data['Age'])

print(f'Средний возраст: {average_age:.2f}, Стандартное отклонение: {std_age:.2f}')
# 2. Создание нового столбца Fare_new
data['Fare_new'] = data['Fare'].apply(lambda x: x * 1.3)

# Проверка результатов
print(data[['Fare', 'Fare_new']].head())
