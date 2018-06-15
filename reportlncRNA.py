#!usr/bin/env python
lines=[line for line in open("/Users/Andy/Desktop/candidate_lncRNA/finallblast.txt")]
target=[]
for line in lines:
	if(float(line.split("\t")[3])>=90)&(float(line.split("\t")[11])<1e-10)&(((float(line.split("\t")[4]))/(float(line.split("\t")[1])))>=0.8):
		target.append(line)
with open("/Users/Andy/Desktop/candidate_lncRNA/newresult.txt","w")as file:
	for line in target:
		file.write(str(line))


