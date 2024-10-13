# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 10:28:59 2024

@author: krivoshein
"""

import psycopg2
import pandas as pd

# Подключение к БД
conn = psycopg2.connect(
    host = "hh-pgsql-public.ebi.ac.uk",
    database = "pfmegrnargs",
    user = "reader",
    password = "NWDMCE5xdipIjRrp"
)
# Создание курсора
cursor = conn.cursor()

# Получение 10 строк из таблицы
cursor.execute("SELECT * FROM rnc_database LIMIT 10;")
rows = cursor.fetchall()
df = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])
print(df)

# Получение нужных столбцов
cursor.execute("SELECT display_name, num_sequences, num_organisms, url FROM rnc_database LIMIT 10;")
filtered_rows = cursor.fetchall()
filtered_df = pd.DataFrame(filtered_rows, columns=['display_name', 'num_sequences', 'num_organisms', 'url'])
print(filtered_df)

cursor.close()
conn.close()