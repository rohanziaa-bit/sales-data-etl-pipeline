import json
import pandas as pd

with open("sales data.json","r") as file:
    data = json.load(file)

df = pd.DataFrame(data['users'])

print (df.head(10   ))

print(df.shape)
print(df.columns)
print(df.info())

print (df.isnull().sum())

print (df['address'].iloc[0])

df['city'] = df['address'].apply(lambda x: x['city'])
print (df['city'].head(10))

df['state'] = df['address'].apply(lambda x: x['state'])
print (df['state'].head(10))

df['country'] = df['address'].apply(lambda x: x['country'])
print (df['country'].head(10))

df['postalCode'] = df['address'].apply(lambda x: x['postalCode'])
print (df['postalCode'].head(10))

print (df['id'].duplicated().sum())

print (df['postalCode'].dtype)
print (df['postalCode'].unique())
print(df['country'].dtype)
print(df['state'].dtype)
print(df['city'].dtype)

print (df['birthDate'].dtype)

df['birthDate'] = pd.to_datetime(df['birthDate'], errors='coerce')
print (df['birthDate'].dtype)

print (df['birthDate'].isnull().sum())

print (df['gender'].unique())

print (df['age'].min())
print (df['age'].max())

print (df['email'].isnull().sum())

print (df['email'].duplicated().sum())

print (df['email'].str.contains("@").sum())


print (df['email'].str.contains(".").sum())

print (df['email'].str.contains("example.com").sum())
print (df['email'].str.contains("outlook.com").sum())

print (df['email'].str.strip('@').sum())

print (df['phone'].isnull().sum())
print (df['phone'].duplicated().sum())

print (df['role'].unique())

df = df.drop(columns=[
    'maidenName',
    'username',
    'password',
    'image',
    'bloodGroup',
    'height',
    'weight',
    'eyeColor',
    'hair',
    'ip',
    'address',
    'macAddress',
    'university',
    'bank',
    'company',
    'ein',
    'ssn',
    'userAgent',
    'crypto'
])

print (df.columns)


with open("sales data.json", "r") as file:
    data = json.load(file)

df.to_csv("cleaned_users.csv", index=False)