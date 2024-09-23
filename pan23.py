import pandas as pd
import numpy as np
data = {
    'eng': [10, 30, 40 ,50],
    'kor': [20, 40, 50, 60],
    'math': [50, 70, 80, 90]
}

df = pd.DataFrame(data, index=['a', 'b', 'c', 'd'])

# print(df)
# print("shape")
# print(df.shape)
# print("shape[0]")
# print(df.shape[0])
# print("ndim")
# print(df.ndim)
# print("size")
# print(df.size)
# print("T")
# print(df.T)
# print(df.index)
# print(df.keys())
# print(df.columns)
# print(df.values)
# print(df.dtypes)
# print(df.dtypes['eng'])
# print(df.info())

# print(df['eng'])
# print(df[['eng', 'math']])
# print(df['eng']['a':'c'])
# print(df[1:3])
# print(df['b':'c'])
# print(df)
# print(df.iloc[0])
# print(df.iloc[0,0])
# print(df.iloc[[0,2,3]])
# print(df.iloc[1:,1])
# print(df.iloc[1:,1:])
# print(df.iloc[1:3,[0,2]])


# print(df.loc['a':'c'])
# print(df.loc[['a','c','d']])
# print(df.loc['b':])
# print(df.loc['b':, 'kor':])
# print(df.loc['b':'c', ['eng','math']])

# print(df)
# print(df+1)
# # print(df+2)
# df['eng'] = [1, 2, 3, 4]
# print(df)
# df['eng'] = df['eng'] + 2
# print(df)
# df.loc['a'] = df.loc['a'] + 2
# print(df)
# df.loc['b': 'c', 'kor':] = [[1, 2], [3, 4]]
# print(df)
# df.loc['b': 'c', 'kor':] = df.loc['b': 'c', 'kor':] + 2

# print(df['eng']>30)
# print(df[df['eng'] > 30])
# print(df[(df['kor'] == 20) | (df['kor'] == 60)])
# print(df[(df['kor'] >= 20) | (df['kor'] <= 60)])
# print(df[df['kor'].isin([20, 40])])

# print(df.query('eng>30'))
# print(df.query('kor==20 or kor==60'))
# print(df.query('20<=kor<=60'))
# num = 30
# print(df.query(f'eng>{num}'))

# print("1")
df['m1'] = [1, 2, 3, 4]
df['m2'] = df['kor'] + df['eng']
print(df)
# print("2")
df.loc['e'] = [1, 2, 3, 4, 5]
print(df)
# print("3")
print(df.drop(index=['a', 'c']))
print(df.drop(columns=['eng','math']))
# print("4")
df.loc['b':'c','kor'] = np.nan
df.loc['c':'d','math'] = np.nan
print(df)
print(df.isna())
print(df.isna().sum())

# ppt pandas 32부터