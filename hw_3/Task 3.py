# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 21:32:30 2024

@author: krivoshein
"""

import pandas as pd

# 1. Считайте датасет из файла train.csv
df = pd.read_csv('train.csv')

# 2. Выведите основную информацию о датасете
print(df.info())
print(df.describe())

# 3. Посчитайте процент выживаемости у каждого класса пассажиров (Pclass)
survival_rate_per_class = df.groupby('Pclass')['Survived'].mean() * 100
print(survival_rate_per_class)

# 4. Выведите самое популярное мужское и самое популярное женское имя на корабле
df['Name'] = df['Name'].str.split(',', expand=True)[1].str.strip()  # Извлекаем имя из строки
df['First_Name'] = df['Name'].str.split('.', expand=True)[0]  # Убираем титул

most_common_male = df[df['Sex'] == 'male']['First_Name'].mode()[0]
most_common_female = df[df['Sex'] == 'female']['First_Name'].mode()[0]
print(f"Самое популярное мужское имя: {most_common_male}")
print(f"Самое популярное женское имя: {most_common_female}")

# 5. Выведите самое популярное мужское и самое популярное женское имя на корабле в каждом классе
popular_names_per_class = df.groupby('Pclass').agg({'First_Name': lambda x: x.mode()[0]})
popular_names_per_class_male = df[df['Sex'] == 'male'].groupby('Pclass')['First_Name'].agg(lambda x: x.mode()[0])
popular_names_per_class_female = df[df['Sex'] == 'female'].groupby('Pclass')['First_Name'].agg(lambda x: x.mode()[0])

print("Самые популярные имена по классам:")
print("Мужские имена:\n", popular_names_per_class_male)
print("Женские имена:\n", popular_names_per_class_female)

# 6. Выведите часть таблицы с пассажирами, возраст которых больше 44 лет
adults_over_44 = df[df['Age'] > 44]
print(adults_over_44)

# 7. Выведите часть таблицы с пассажирами, возраст которых меньше 44 лет и которые мужского пола
young_male_passengers = df[(df['Age'] < 44) & (df['Sex'] == 'male')]
print(young_male_passengers)

# 8. Выведите количества n-местных кабин (в которых было 2, 3, 4, ... человека)
cabin_counts = df['Cabin'].dropna().str.split(' ', expand=True).stack().value_counts()
print(cabin_counts)