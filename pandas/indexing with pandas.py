import pandas as pd

datas=[100,200,230,123,523.2,94.3,273]
indexes=["ram","sam","jodu","modhu","apt1","apt2","apt3"]

combined=pd.Series(datas,index=indexes)
print(combined)
for i in range(7):
    print(combined.iloc[i])
combined.loc["apt1"]=23
print(combined.loc["apt1"])

