import os
import pandas as pd

os.chdir("/Users/Andy/Desktop")

ID_list = []
with open('Uterus_bio_bai_num.txt', 'r') as f1:
    con = f1.readlines()
    for line in con:
        line = line.strip()
        ID_list.append(line.split('\t')[0])


list_bladder = [x for x in list(data.columns) if x[0:7] == 'Bladder']
data_filter1 = data.loc[:,list_bladder]
ID_name = ['ENSG00000187244.9' ,'ENSG00000089220.4', 'ENSG00000168878.15']
data_filter2 = data_filter1.loc[ID_name, :]

data_filter2.to_csv('result.txt',sep='\t')
