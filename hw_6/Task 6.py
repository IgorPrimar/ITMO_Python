# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 08:25:02 2024

@author: krivoshein
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score


data = pd.read_csv('train.csv')

   # Предварительная обработка: удаление ненужных столбцов и работа с пропусками
data.drop(['Name', 'Ticket', 'Cabin'], axis=1, inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)
data['Age'].fillna(data['Age'].median(), inplace=True)
data = pd.get_dummies(data, columns=['Sex', 'Embarked'], drop_first=True)
X = data.drop('Survived', axis=1)
y = data['Survived']

   # Разделение на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#Масштабирование признаков:
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

#Обучение бейзлайн модели (например, случайного предсказания)
baseline_pred = np.random.randint(0, 2, size=y_test.shape)
baseline_f1 = f1_score(y_test, baseline_pred)
print(f"Baseline F1 Score: {baseline_f1:.2f}")

#Обучение модели логистической регрессии
model = LogisticRegression()
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)

   # Оценка качества модели
f1 = f1_score(y_test, y_pred)
print(f"Logistic Regression F1 Score: {f1:.2f}")
