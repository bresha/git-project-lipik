from os import name
import pandas as pd
s = pd.Series(['Hrvoje', 'Matija'])
print(type(s))


s.name = 'Ekipa'
print(type(s.values))
print(type(s.name))
print(s.index)
print(s[1])
print(s)


s.index = ['prvi', 'drugi']
print(s.index)

s.prvi = 'Darko'
print(s)

for i, v in s.items():
    print(i, v)
    if 'd' in v.lower():
        s[i] = 'Hrvoje'

print(s)


df = pd.DataFrame(
    {
        'Grad': ['Slavonski Brod', 'Koprivnica'],
        'godine_iskustva': [40, 25],
        s.name: s.values
    },
    columns = ['Grad', 'godine_iskustva', s.name]
)
print(df)

print(df.columns)

df.index = ['prvi', 'drugi']

print(df.Grad['prvi'])

print(df.info())

print(df.shape)

print(df.size)

print(df.describe())