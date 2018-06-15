#!usr/bin/python
import sys
lncnum0=lncnum1=lncnum2=lncnum3=lncnum4=lncnum5=lncnum6=lncnum7=lncnum8=lncnum9=lncnum10=lncnummore=0
for i in open('/share/Public/stu_gwang/newMaize/DRAW/getorf_xiaomi_candidate_lncRNA.exonCount.txt'):
	if 'exonCount' not in i:
		continue
	if 'exonCount=0\n' in i:
		lncnum0+= 1
	else:
		if 'exonCount=1\n' in i:
			lncnum1+=1
		else:
			if 'exonCount=2\n' in i:
				lncnum2+=1
			else:
				if 'exonCount=3\n' in i:
					lncnum3+=1
				else:
					if 'exonCount=4\n' in i:
						lncnum4+=1
					else:
						if 'exonCount=5\n' in i:
							lncnum5+=1
						else:
							if 'exonCount=6\n' in i:
								lncnum6+=1
							else:
								if 'exonCount=7\n' in i:
									lncnum7+=1
								else:
									if 'exonCount=8\n' in i:
										lncnum8+=1
									else:
										if 'exonCount=9\n' in i:
											lncnum9+=1
										else:
											if 'exonCount=10\n' in i:
												lncnum10+=1
											else:
												lncnummore+=1
with open('/share/Public/stu_gwang/newMaize/DRAW/lncnum.txt','a')as file:
	file.write("lncnum1="+str(lncnum1)+"\n"+"lncnum2="+str(lncnum2)+"\n"+"lncnum3="+str(lncnum3)+"\n"+"lncnum4="+str(lncnum4)+"\n"+"lncnum5="+str(lncnum5)+"\n"+"lncnum6="+str(lncnum6)+"\n"+"lncnum7="+str(lncnum7)+"\n"+"lncnum8="+str(lncnum8)+"\n"+"lncnum9="+str(lncnum9)+"\n"+"lncnummore="+str(lncnummore))

		
	
	
