"""
@author bharat arora
"""
import csv
import numpy as np
import pandas as pd
import os 
import math

pred = pd.read_csv("Formated_data_corrected.csv")

pred_header = list(pred)

num_parameters=len(pred_header)
each_wgt=1.0/num_parameters
out_header = []

u="node_1"
v="node_2"
w="weight"
out_header.append(u)
out_header.append(v)
out_header.append(w)

output_file='out2.csv'

if output_file in os.listdir(os.getcwd()):
	os.remove(output_file)
csvfile=open(output_file, 'a')

fieldnames =  out_header

writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writeheader()

num_nodes = 1946
for i in range(0,num_nodes):
	for j in range(i+1,num_nodes):
		dic={}
		dic[u]=i+1;
		dic[v]=j+1;
		dot_pro=each_wgt;
		for param in pred_header:
			x=pred.iloc[i][param]
			y=pred.iloc[j][param]			
			if(param=="Sno" or x=="Nan" or y=="Nan"):
				continue;
			elif(type(x)==type("xyz")):
				if(x==y):
					dot_pro+=each_wgt
			else:
				if(param=="attacker"):
					dot_pro=dot_pro+(x*y*each_wgt)/53
				elif(param=="defender"):
					dot_pro=dot_pro+(x*y*each_wgt)/39
				elif(param=="popularity"):
					if(x!=0 or y!=0):
						dot_pro=dot_pro-abs(x-y)*each_wgt*(1/math.sqrt(x*x+y*y))
				else:
					dot_pro=dot_pro+(x*y*each_wgt)
		dic[w]=dot_pro
		writer.writerow(dic)