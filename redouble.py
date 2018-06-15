#!usr/bin/python3
lines=[line for line in open ("/Users/Andy/Desktop/id.txt")]
target=[]
for a in lines:
	if a not in target:
		target.append(a)
with open("id2.txt","w")as file:
	for i in target:
		file.write(i)
