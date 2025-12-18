import pandas as pd

poke_data={"name":["bulbasaur","charizard","squirtle","pikachu","sandshrew","ditto","dragonite","vulpix"],
           "total":[372,303,278,399,256,283,267,284],
           "attack":[52,34,56,76,99,56,43,76],
           "defense":[100,120,80,67,89,111,105,95]}
poke_index=["pokemon1","pokemon2","pokemon3","pokemon4","pokemon5","pokemon6","pokemon7","pokemon8"]
df=pd.DataFrame(poke_data,index=poke_index)

#adding col

df["speed"]=[58,78,78,45,30,70,50,145]
print(df)

#adding row

pokemon_name=input("ener a pokemon name: ")
total=int(input("enter the health: "))
attack=int(input("enter the attack: "))
defense=int(input("enter the defense: "))
speed=int(input("enter the speed: "))

new_poke_data=pd.DataFrame([{"name":pokemon_name,"total":total,"attack":attack,"defense":defense,"speed":speed}],index=["pokemon9"])
df=pd.concat([df,new_poke_data])
print(df)