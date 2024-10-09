# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 09:42:58 2024

@author: krivoshein
"""

import polars as pl

# Загрузка датасета
df = pl.read_csv("train.csv")

# Вывод основной информации о датасете
print(df.describe())
print(df.dtypes)
print(df.null_count())
print(df.mean())

# Посчет количества пассажиров каждого класса (Pclass)
pclass_counts = df.get_column("Pclass").value_counts()
print("Посчет количества пассажиров каждого класса:\n", pclass_counts)

# Вывод части таблицы с пассажирами, возраст которых больше 44 лет
older_passengers = df.filter(pl.col("Age") > 44)
print("Пассажираы, возраст которых больше 44 лет:\n", older_passengers)

# Вывод количества выживших мужчин и женщин
survival_counts = (df.filter(pl.col("Survived") == 1).group_by("Sex").agg(pl.count()).sort("Sex"))
print("Вывод количества выживших мужчин и женщин:\n", survival_counts)

