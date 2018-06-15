#!usr/bin/python
import sys,re
name=sys.argv[2]
flag=0
target=[]
for line1 in name:
	target.append(re.findall(r'PB.*?f1p99',line1))
with open(sys.argv[1])as file:
	for line in file:
		if line[0]=='>':
			if re.findall(r'PB.*?f1p99',line) in target:
				flag=1
				with open('/share/Public/stu_gwang/newlncRNA/biduishang.txt','a')as file:
					file.write(line)
			else:
				flag=0
				with open('/share/Public/stu_gwang/newlncRNA/meibiduishang.txt','a')as file:
					file.write(line)
		else:
			if flag==1:
				with open('/share/Public/stu_gwang/newlncRNA/biduishang.txt','a')as file:
					file.write(line)
			else:
				with open('/share/Public/stu_gwang/newlncRNA/meibiduishang.txt','a')as file:
					file.write(line)
