import numpy as np
import pandas as pd
import csv

predictions = pd.read_csv("predictions.csv")


freq = {}
count=0
nan_count=0
for y in list(predictions.title):
	if pd.isnull(y):
		nan_count+=1.0
		continue
	if freq.has_key(y):
		freq[y]+=1.0
		count+=1.0
	else: 
		freq[y]=1.0
		count+=1.0
	

# total values
total = nan_count+count
# print total

relative_freq={}
for y in freq:
	relative_freq[y]=freq[y]*100/total

# this is to print the relative relative_freq of different titles 
# for y in relative_freq:
# 	print y,relative_freq[y]	
# print "nan title",nan_count*100/total

# assumption rare the title is more is its imporantce

imp={}
for y in relative_freq:
	imp[y]=1/relative_freq[y]


# print sorted(imp.values())
for y in imp:
	print y,"\t\t",imp[y]
print "nan",total/(nan_count*100)

with open('names.csv', 'w') as csvfile:
    fieldnames = ['title', 'importance']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for y in imp:
    	writer.writerow({'title': y , 'importance': imp[y]})