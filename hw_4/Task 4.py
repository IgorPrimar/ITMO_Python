# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 23:03:35 2024

@author: krivoshein
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


data = pd.read_csv('train.csv')
sns.set(style='whitegrid')
fig, axes = plt.subplots(2, 2, figsize=(10, 5))

#Распределение значений признаков Survived, Pclass, Age, Sex, Parch
# Survived
sns.countplot(x='Survived', data=data, ax=axes[0, 0])
axes[0, 0].set_title('Распределение выживаемости (Survived)')
axes[0, 0].set_xlabel('Выживаемость')
axes[0, 0].set_ylabel('Количество пассажиров')

# Pclass
sns.countplot(x='Pclass', data=data, ax=axes[0, 1])
axes[0, 1].set_title('Распределение классов (Pclass)')
axes[0, 1].set_xlabel('Класс')
axes[0, 1].set_ylabel('Количество пассажиров')

# Age (гистограмма)
sns.histplot(data['Age'].dropna(), bins=30, ax=axes[1, 0], kde=True)
axes[1, 0].set_title('Распределение возраста (Age)')
axes[1, 0].set_xlabel('Возраст')
axes[1, 0].set_ylabel('Количество пассажиров')

# Sex
sns.countplot(x='Sex', data=data, ax=axes[1, 1])
axes[1, 1].set_title('Распределение по полу (Sex)')
axes[1, 1].set_xlabel('Пол')
axes[1, 1].set_ylabel('Количество пассажиров')

plt.tight_layout()
plt.show()

#График типа boxplot для столбца Age
plt.figure(figsize=(8, 6))
sns.boxplot(y='Age', data=data)
plt.title('Boxplot возраста пассажиров (Age)')
plt.ylabel('Возраст')
plt.show()

#график типа pie chart для переменных Survived, Pclass, подпишите доли в процентах
# Pie chart for Survived
plt.figure(figsize=(8, 6))
data['Survived'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Доля выживших и невыживших')
plt.ylabel('')
plt.show()

# Pie chart for Pclass
plt.figure(figsize=(8, 6))
data['Pclass'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Доля пассажиров по классам')
plt.ylabel('')
plt.show()

#график типа pairplot для всех числовых переменных датасета
sns.pairplot(data.select_dtypes(include=['float64', 'int64']))
plt.title('Парные графики для числовых переменных')
plt.show()

#интерактивный sunburst plot с помощью plotly
sunburst_data = data.groupby(['Pclass', 'Sex']).size().reset_index(name='count')
fig = px.sunburst(sunburst_data, path=['Pclass', 'Sex'], values='count',
                  title='Распределение пассажиров по классам и полу')
fig.show()