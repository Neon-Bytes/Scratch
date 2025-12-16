import pandas as pd

calories={"day1":1750,
          "day2":456,
          "day3":2100,
          "day4":234}
series=pd.Series(calories)


series.loc["day4"]+=300
print(series.loc["day3"])
print(series.loc["day4"]) 

print(series)

print(series[series>1500])