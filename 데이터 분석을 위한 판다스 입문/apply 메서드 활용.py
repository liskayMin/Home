import pandas as pd

def my_sq(x):
    return x**2

def my_exp(x,n):
    return x ** n

df = pd.DataFrame({'a':[10,20,30],'b':[20,30,40]})
# print(df)
# print(df['a']**2)

# sq = df['a'].apply(my_sq)
# print(sq)
# ex = df['a'].apply(my_exp, n=2)
# print(ex)

def print_me(x):
    print(x)

# print(df.apply(print_me, axis = 0)) # 열
# print(df.apply(print_me, axis = 1)) # 행

# def avg_3(x,y,z):
#     return (x+y+z)/3
# print(df.apply(avg_3)) # 이러면 TypeError가 생김 -> col로 해야함

def avg_3_apply(col):
    x = col[0]
    y = col[1]
    z = col[2]
    return (x+y+z)/3
# print(df['a'])
# print(df.shape)
# print(df.apply(avg_3_apply))

def avg_2_apply(row):
    sum =0
    for item in row:
        sum += item
    return sum / df.shape[1]

# print(df.apply(avg_2_apply, axis=1))

import seaborn as sns
titanic = sns.load_dataset("titanic")

# print(titanic)
# print(titanic.info())

import numpy as np

def count_missing(vec):
    print(vec)
    null_vec = pd.isnull(vec)
    print(null_vec)
    null_count = np.sum(null_vec)
    print(null_count)
    return null_count

cmis_col = titanic.apply(count_missing)
# print(cmis_col)

def prop_missing(vec):
    num = count_missing(vec)
    dem = vec.size
    return num / dem

pmis_col = titanic.apply(prop_missing)
# print(pmis_col)

def prop_complete(vec):
    return 1-prop_missing(vec)