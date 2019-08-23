
import csv
import operator
import os
readfile=open('equal_weighted_attribute_graph_sorted.csv','r')
graph = csv.reader(readfile, delimiter=',', quotechar='|')


output_file='equal_weighted_attribute_graph_top6K.csv'

if output_file in os.listdir(os.getcwd()):
	os.remove(output_file)

count=0
writefile = open(output_file,'wb')
csvwriter = csv.writer(writefile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
csvwriter.writerow(['Source','Target','Weight'])
for row in graph:
	if(count==6000):
		break;
	csvwriter.writerow(row)
	count=count+1
