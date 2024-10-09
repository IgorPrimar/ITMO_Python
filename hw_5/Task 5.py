# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 16:28:16 2024

@author: krivoshein
"""
import pandas as pd

df = pd.read_csv('Housing.csv')
print(df.info())
df = df.fillna(0)
# Выводим потребление памяти до оптимизации
memory_before = df.memory_usage(deep=True).sum()

# Оптимизация типов данных
for col in df.select_dtypes(include=['float64']).columns:
    if (df[col].min() >= -3.4e38) and (df[col].max() <= 3.4e38):
        df[col] = df[col].astype('float16')  # Используем float32 вместо float16
    else:
        print(f'Warning: {col} имеет значения, не подходящие для float16')
  
for col in df.select_dtypes(include=['object']).columns:
    df[col] = df[col].astype('category')

memory_after = df.memory_usage(deep=True).sum()

print(f'Память до оптимизации: {memory_before} байт')
print(f'Память после оптимизации: {memory_after} байт')

