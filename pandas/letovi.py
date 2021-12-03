import pandas as pd
import numpy as np
import os
from datetime import date


# 1. Loadaj Deanovu tablicu (pazi na header)
df = pd.read_csv(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'letovi.csv'))


# 2. Prikaži podatke o tablici
print(df.head())
print(df.columns)
print(df.shape)
print(df.size)
print(df.describe())
print(df.dtypes)


# 3. Pretvori column sa cijenama u dva nova:
    # a) numeričke vrijednosti (napravi konverzije u EUR ili bilo koju drugu valutu) 
    # b) drugi stupac gdje piše valuta
df['price'] = df['Prices'].map(lambda x: float(x.split(' ')[0].replace('.', '')) / 7.3)
df.insert(7, 'currency', 'EUR')
print(df.head())


# 4. Dodajte novi stupac gdje piše trajanje putovanja (arrival minus departure)
    # stavite 1h ako je trajanje dana 0
def convert_date(x):
    months = {
        'Dec': 12,
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4
    }
    date_list = x.split(' ')
    day = int(date_list[1])
    month_str = date_list[2]
    month = months[month_str]
    year = 2021 if month == 12 else 2022
    return date(year, month, day)

df['departure'] = pd.Series(map(convert_date, df['Departure date:']))
df['arrival'] = pd.Series(map(convert_date, df['Date of Arrival:']))
df['difference'] = np.where(df['arrival'] - df['departure'] > pd.Timedelta(value=0, unit='D'), (df['arrival'] - df['departure']), np.timedelta64(3600000000000, 'ns'))
print(df.head())


# 5. Pronađi najpovoljni let srijedom
df['day'] = df['Date of Arrival:'].map(lambda x: x.split(' ')[0])
print(df.head())
sorted_df = df.sort_values(['price'], ascending=True)
print(sorted_df[sorted_df['day'] == 'Wed'].head(1))