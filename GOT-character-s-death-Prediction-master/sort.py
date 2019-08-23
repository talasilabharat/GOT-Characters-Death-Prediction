
import csv
import operator
import os
readfile=open('equal_weighted_attribute_graph.csv','r')
graph = csv.reader(readfile, delimiter=',', quotechar='|')

next(readfile, None)

sortedlist = sorted(graph, key=lambda row: float(row[2]) , reverse=True)


output_file='equal_weighted_attribute_graph_sorted.csv'

if output_file in os.listdir(os.getcwd()):
	os.remove(output_file)

writefile = open(output_file,'wb')
csvwriter = csv.writer(writefile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
for row in sortedlist:
	csvwriter.writerow(row)