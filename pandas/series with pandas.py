import pandas as pd

data=[100,102,104]
data1=[100.1,101.1,102.2]
data2=["1","2","Good","bad"]
data3=[True,False,True]

series=pd.Series(data,index=["apartment1","apartment2","aparment3"])
series1=pd.Series(data1)
series2=pd.Series(data2)
series3=pd.Series(data3)

print(data)
print(series.loc["apartment2"])
print(series)
print(series1)
print(series2)
print(series3)