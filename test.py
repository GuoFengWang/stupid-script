#!usr/bin/python3
import re
with open("/share/Public/stu_gwang/newlncRNA/all_quiver.collapsed.rep.fa","r")as file:
	f=file.read()
	lis=f.split(">")
	dic={}
	for i in lis:
		c=re.findall(r'^PB.*?\n',i)
		b=re.findall(r'[atgc]+\n',i,re.I)
		e=''.join(map(str,b))
		d=str(c).strip('[]')
		dic[d]=e    
with open("/share/Public/stu_gwang/newlncRNA/id2.txt","r")as file:
	f1=file.readlines()
	lis_key=dic.keys()
	dic_f1={}
	for g in f1:
		dic_f1[g]=1
	f1_key=dic_f1.keys()
	targetf1=[]
	for h in f1_key:
		targetf1.append(re.findall(r'PB.*f1p\d\d',h))
	targetdic=[]
	for k in lis_key:
		targetdic.append(re.findall(r'PB.*?f1p\d\d',k))
		
	
	
	with open("/share/Public/stu_gwang/newlncRNA/biduishang.txt","w")as file:
		for i in targetf1:
			for j in targetdic:
				if i==j:
					file.write(i+dic[i])
	with open("/share/Public/stu_gwang/newlncRNA/meibiduishang.txt","w")as file:
		for i in f1:
			for j in lis_key:
				if not i==j.strip(""):
					file.write(j+dic[j])
				
			
		
