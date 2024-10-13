# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:06:44 2024

@author: krivoshein
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import streamlit as st

# Загрузка данных
data = pd.read_csv('realty_data.csv')
print(data.head())
print(data.isnull().sum())
data['total_square'] = data['total_square'].fillna(data['total_square'].mean())
data['rooms'] = data['rooms'].fillna(data['rooms'].mean())
data['price'] = data['price'].fillna(data['price'].mean())
X = data[['total_square', 'rooms']]
y = data['price']

# Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучение модели
model = LinearRegression()
model.fit(X_train, y_train)
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)
    #with open('model.pkl', 'rb') as model_file:
        #model = pickle.load(model_file)

# Заголовок приложения
st.title('Прогнозирование стоимости недвижимости')

# Ввод признаков
area = st.number_input('Площадь (кв. м):', min_value=0)
rooms = st.number_input('Количество комнат:', min_value=1)

# Кнопка прогноза
if st.button('Предсказать'):
    prediction = model.predict([[area, rooms]])
    st.write(f'Прогнозируемая стоимость: {prediction[0]:.2f} рублей')
