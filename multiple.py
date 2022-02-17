import pandas as pd
series1=pd.Series([2,4,6,8.9],index=['a','b','c','d'])
print(series1)
print(series1['c'])
print(series1[['a','b','d']])
      