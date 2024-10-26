# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:06:44 2024

@author: krivoshein
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
from fastapi import FastAPI
from pydantic import BaseModel


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

# Сохранение модели
joblib.dump(model, 'housing_model.pkl')
# Создание экземпляра FastAPI
app = FastAPI()

# Загрузка модели
model = joblib.load('housing_model.pkl')

# Определение модели данных для входных данных
class House(BaseModel):
    area: float
    bedrooms: int

# Реализация метода получения предсказания
@app.post('/predict/')
def predict(house: House):
    data = [[house.area, house.bedrooms]]
    prediction = model.predict(data)
    return {"predicted_price": prediction[0]}

# Реализация эндпоинта для GET-запроса
@app.get('/predict_get/')
def predict_get(area: float, bedrooms: int):
    data = [[area, bedrooms]]
    prediction = model.predict(data)
    return {"predicted_price": prediction[0]}

# Реализация liveness-пробы (health-check)
@app.get('/health')
def health_check():
    return {"status": "up"}

