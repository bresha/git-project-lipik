import pandas as pd
import numpy as np
import os
from datetime import date

from pandas._libs.tslibs.timedeltas import Timedelta

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

# df['difference_in_hours'] = np.where(df['arrival'] - df['departure'] > 0, (df['arrival'] - df['departure']) * 24, 1)
df['difference_in_hours'] = np.where(df['arrival'] - df['departure'] > pd.Timedelta(value=0, unit='D'), pd.to_timedelta((df['arrival'] - df['departure']), 'ns'), pd.to_timedelta(1, 'h'))
# df['difference_in_hours'] = df['arrival'] - df['departure']
print(df.head())
# df['difference_in_hours'] = df['difference_in_hours'] / 3600000000000
# print(df.head)
# df['day'] = df['Date of Arrival:'].map(lambda x: x.split(' ')[0])
# print(df.head())

# sorted_df = df.sort_values(['price'], ascending=True)
# print(sorted_df)
# print(sorted_df[sorted_df['day'] == 'Wed'].head(1))