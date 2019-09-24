#encoding: utf-8

import pandas as pd 
import numpy as np

data = {
	"food": ["bacon", "pulled pork", "bacon", "Pastrami", "corned beef", "Bacon", "pastrmi", "honey ham", "nova lox"],
	"ounces": [4.0, 3.0, None, 6.0, 7.5, 8.0, -3.0, 5.0, 6.0],
	"animal": ["pig", "pig", "pig", "cow", "cow", "pig", "cow", "pig", "salmon"]
}


df1 = pd.DataFrame(data, index=[1, 2, 3, 4, 5, 6, 7, 8, 9])
print(df1)
"""
          food  ounces  animal
1        bacon     4.0     pig
2  pulled pork     3.0     pig
3        bacon     NaN     pig
4     Pastrami     6.0     cow
5  corned beef     7.5     cow
6        Bacon     8.0     pig
7      pastrmi    -3.0     cow
8    honey ham     5.0     pig
9     nova lox     6.0  salmon
"""
# 把没有数据的行删除
df2 = df1.dropna(how="any", axis=0)

# 删除有负值的行
t = df2[df2["ounces"] < 0].index
df3 = df2.drop(index=t)

# 统一“food”列的大小写
df3["food"] = df3["food"].str.title()
df3["animal"] = df3["animal"].str.title()

print(df3)
"""
          food  ounces  animal
1        Bacon     4.0     Pig
2  Pulled Pork     3.0     Pig
4     Pastrami     6.0     Cow
5  Corned Beef     7.5     Cow
6        Bacon     8.0     Pig
8    Honey Ham     5.0     Pig
9     Nova Lox     6.0  Salmon
"""
