import pandas as pd

name_age = {'name': ['Riyansh', 'Manish', 'Nitesh'],
            'age': [1, 4, 13]}

df = pd.DataFrame(name_age, index=['a', 'b', 'c'])  # by default index 0,1 2 and replaced by 0,1,2
# print(df)
# print(df.loc[0])
print(df.loc['a'])
print(df.loc[['a']])
