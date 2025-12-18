import pandas as pd

data={"name":["arjun","karna","duryodhan","bishma-pitama"],
      "age":[34,36,53,102]}
index=["Emp1","Emp2","Emp3","Emp4"]
df=pd.DataFrame(data,index=index)
print(df.loc["Emp3"])    #getting location through made up index

df["job"]=["Archery","Warrior","Cyclist","Footballer"]     #adding a column
print(df)

#adding a row

new_row=pd.DataFrame([{"name":"Abhimanyu","age":16,"job":"Greatest"},
                      {"name":"Dronacharya","age":89,"job":"Teacher"}],
                      index=["Emp4","Emp5"])
df=pd.concat([df,new_row])
print(df)