import pandas as pd
import numpy as np
import os

df = pd.read_csv(os.path.join(os.getcwd(), 'letovi.csv'))
print(df.head())
print(df.columns)
print(df.shape)
print(df.size)
print(df.describe())
print(df.dtypes)

df['price'] = df['Prices'].map(lambda x: float(x.split(' ')[0].replace('.', '')) / 7.3)
df.insert(7, 'currency', 'EUR')
print(df.head())

def convert_date(x):
    date_list = x.split(' ')
    day = date_list[1]
    return int(day)

df['departure'] = pd.Series(map(convert_date, df['Departure date:']))
df['arrival'] = pd.Series(map(convert_date, df['Date of Arrival:']))

df['difference_in_hours'] = np.where(df['arrival'] - df['departure'] > 0, (df['arrival'] - df['departure']) * 24, 1)

df['day'] = df['Date of Arrival:'].map(lambda x: x.split(' ')[0])
print(df.head())

sorted_df = df.sort_values(['price'], ascending=True)
print(sorted_df)
print(sorted_df[sorted_df['day'] == 'Wed'].head(1))