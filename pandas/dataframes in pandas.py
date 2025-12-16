import pandas as pd

data={"name":["arjun","karna","duryodhan","bishma-pitama"],
      "age":[34,36,53,102]}

df=pd.DataFrame(data)

print(df)
print(df.loc[2])