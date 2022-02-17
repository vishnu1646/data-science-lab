import pandas as pd
s=pd.Series([1,2,3,4,5,6],index=['a','b','c','d','e','f'])
print(s.head(2))
print(s.tail(4))