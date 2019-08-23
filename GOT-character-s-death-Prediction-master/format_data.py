import csv
import numpy as np
import pandas as pd
import os 

pred = pd.read_csv("final-prediction.csv")
battle = pd.read_csv("final-battle.csv")


pred_header = list(pred)
battle_name = list(battle.Battle_name)

out_header = pred_header + battle_name
a="attacker"
d="defender"
out_header.append(a)
out_header.append(d)

output_file='out1.csv'
if output_file in os.listdir(os.getcwd()):
	os.remove(output_file)
csvfile=open(output_file, 'a')

fieldnames =  out_header
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

for i in range(0,1946):
	dic={}
	for y in pred_header:
		x=pred.iloc[i][y]
		dic[y]=x
	for y in battle_name:
		dic[y]=0
	dic[a]=0
	dic[d]=0
	if dic["house"]!="Nan":
		for j in range(0,38):
			if dic["house"].lower()!="Nan":
				if dic["house"].lower()==battle.iloc[j].attacker_1.lower():
					dic[battle.iloc[1].Battle_name]=1
					dic[a]+=1
				if dic["house"].lower()==battle.iloc[j].attacker_2.lower():
					dic[battle.iloc[1].Battle_name]=1
					dic[a]+=1
				if dic["house"].lower()==battle.iloc[j].attacker_3.lower():
					dic[battle.iloc[1].Battle_name]=1
					dic[a]+=1
				if dic["house"].lower()==battle.iloc[j].attacker_4.lower():
					dic[battle.iloc[1].Battle_name]=1
					dic[a]+=1
				if dic["house"].lower()==battle.iloc[j].defender_1.lower():
					dic[battle.iloc[1].Battle_name]=1
					dic[d]+=1
				if dic["house"].lower()==battle.iloc[j].defender_2.lower():
					dic[battle.iloc[1].Battle_name]=1
					dic[d]+=1
				if dic["house"].lower()==battle.iloc[j].defender_3.lower():
					dic[battle.iloc[1].Battle_name]=1
					dic[d]+=1
				if dic["house"].lower()==battle.iloc[j].defender_4.lower():
					dic[battle.iloc[1].Battle_name]=1
					dic[d]+=1
	writer.writerow(dic)