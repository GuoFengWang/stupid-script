#!usr/bin/python
lines=[line for line in open("/Users/Andy/Desktop/newresult.txt")]
target=[]
for eles in lines:
	target.append(eles.split("\t")[0])
with open("id.txt","w")as file:
	for a in target:
		file.write(str(a)+"\n")
