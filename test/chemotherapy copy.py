import pandas as pd 
import openpyxl, os, re
import pprint
from collections import OrderedDict 
project_file = '/Users/andy/Desktop/test/临床样本项目信息/临床样本项目信息3.4.xlsx' #项目信息文件表
mypath = '/Users/andy/Desktop/test/输入文件存放目录' #提取基因型文件存放目录
project_dic = {} #存储客户姓名——项目编号及所做项目信息
for i in os.listdir(mypath):
    info_data = pd.read_excel(project_file)
    if i != '.DS_Store':
        project_dic[info_data.loc[info_data['样本编号']==i.split('.')[0], '患者姓名'].all()] = \
        info_data.loc[info_data['样本编号']==i.split('.')[0], '检测项目'].all() + '--' + i
        


def dic_output(db_path):
    name_cancer = pd.read_excel(db_path)
    new_name_cancer = name_cancer.fillna(axis=0, method='ffill')
    dic_name_cancer = {}
    for rs_id in name_cancer['位点'].unique():
        if type(rs_id) == str:
            dic_name_cancer[rs_id] = new_name_cancer.loc[new_name_cancer['位点']==rs_id, '基因型'].unique()
    return dic_name_cancer



def correctGT(input_file, dic_name):
    data = pd.read_csv(input_file, sep='\t')
    list_correctGT = {}
    reverse_complement = lambda gt: gt.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g').upper()[::-1]
    complement = lambda gt: gt.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()
    for key in dic_name.keys():
        if data.loc[data['RSID']==key, 'Genotype'].empty == True:
            #list_correctGT.append(key + '--' + '基因型不存在')
            #list_correctGT[key] = '基因型不存在'
            list_correctGT[key] = dic_name[key][1]
        else:
            if data.loc[data['RSID']==key, 'Genotype'].all() in dic_name[key]:
                #list_correctGT.append(key + '--' + data.loc[data['RSID']==key, 'Genotype'].all())
                list_correctGT[key] = data.loc[data['RSID']==key, 'Genotype'].all()
            elif complement(data.loc[data['RSID']==key, 'Genotype'].all()) in dic_name[key]:
                #list_correctGT.append(key + '--' + complement(data.loc[data['RSID']==key, 'Genotype'].all()))
                list_correctGT[key] = complement(data.loc[data['RSID']==key, 'Genotype'].all())
            elif reverse_complement(data.loc[data['RSID']==key, 'Genotype'].all()) in dic_name[key]:
                #list_correctGT.append(key + '--' + reverse_complement(data.loc[data['RSID']==key, 'Genotype'].all()))
                list_correctGT[key] = reverse_complement(data.loc[data['RSID']==key, 'Genotype'].all())
            elif data.loc[data['RSID']==key, 'Genotype'].all()[::-1] in dic_name[key]:
                #list_correctGT.append(key + '--' + data.loc[data['RSID']==key, 'Genotype'].all()[::-1])
                list_correctGT[key] = data.loc[data['RSID']==key, 'Genotype'].all()[::-1]

            elif '6' or '7' in data.loc[data['RSID']==key, 'Genotype'].all():
                if data.loc[data['RSID']==key, 'Genotype'].all().count('6') == 1:
                    #list_correctGT.append(key + '--' + '(TA)6/(TA)7')
                    list_correctGT[key] = '(TA)6/(TA)7'
                elif data.loc[data['RSID']==key, 'Genotype'].all().count('6') == 2:
                    #list_correctGT.append(key + '--' + '(TA)6/(TA)6')
                    list_correctGT[key] = '(TA)6/(TA)6'
                elif data.loc[data['RSID']==key, 'Genotype'].all().count('6') == 0:
                    #list_correctGT.append(key + '--' + '(TA)7/(TA)7')
                    list_correctGT[key] = '(TA)7/(TA)7'
    return list_correctGT





dic_path = {'gene_37':'/Users/andy/Desktop/test/数据库文件/肺癌37基因数据库12.30.xlsx',
'gene_50':'/Users/andy/Desktop/test/数据库文件/泛癌种50基因.xlsx',
'gene_500':'/Users/andy/Desktop/test/数据库文件/500基因数据库.xlsx',
'gene_aitong':'/Users/andy/Desktop/test/数据库文件/癌痛药物数据库.xlsx',
'gene_aitong500':'/Users/andy/Desktop/test/数据库文件/癌痛药物数据库-500基因.xlsx',
'gene_chang37':'/Users/andy/Desktop/test/数据库文件/肠癌37数据库(1).xlsx'}


dic_37gene = dic_output(dic_path['gene_37'])
dic_50gene = dic_output(dic_path['gene_50'])
dic_500gene = dic_output(dic_path['gene_500'])
dic_aitong = dic_output(dic_path['gene_aitong'])
dic_aitong500 = dic_output(dic_path['gene_aitong500'])
dic_chang37 = dic_output(dic_path['gene_chang37'])
#dic_37gene = dic_output('/Users/andy/Desktop/化疗药/肺癌化疗37基因/肺癌37基因数据库/肺癌37基因数据库12.30.xlsx')
#dic_50gene = dic_output('/Users/andy/Desktop/化疗药/泛癌种50基因/泛癌种50基因数据库/泛癌种50基因.xlsx')
#dic_500gene = dic_output('/Users/andy/Desktop/化疗药/泛癌种500基因化疗/500基因数据库/500基因数据库.xlsx')
#dic_aitong = dic_output('/Users/andy/Desktop/化疗药/癌痛/癌痛药物数据库.xlsx')
#dic_aitong500 = dic_output('/Users/andy/Desktop/化疗药/癌痛/癌痛药物数据库-500基因.xlsx')
#dic_chang37 = dic_output('/Users/andy/Desktop/化疗药/肠癌化疗37基因/肠癌37数据库(1).xlsx')
#data37 = pd.read_excel('/Users/andy/Desktop/化疗药/肺癌化疗37基因/肺癌37基因数据库/肺癌37基因数据库12.30.xlsx')
#new_data37 = data37.fillna(axis=0, method='ffill')
#dic_37gene = {}
#for rs_id in data37['位点'].unique():
#    if type(rs_id) == str:
#        dic_37gene[rs_id] = new_data37.loc[new_data37['位点']==rs_id, '基因型'].unique()
#print (dic_37gene)

#if 'hh' in dic_37gene['rs1695']:
#    print('yes')
#else:
#    print('no')

gene_37 = {}
gene_50 = {}
gene_500 = {}
gene_aitong = {}
gene_aitong500 = {}
gene_chang37 = {}


        
for name in project_dic.keys():
    if '肺癌37基因（靶向+化疗+癌痛）' in project_dic[name].split('--')[0] or '肺癌37基因(靶向+癌痛)' in project_dic[name].split('--')[0]:
        gene_37['gene_37'+'__'+name+'--'+project_dic[name].split('--')[1].split('.')[0]] = correctGT(mypath+'/'+project_dic[name].split('--')[1], dic_37gene)
        gene_aitong['gene_aitong'+'__'+name+'--'+project_dic[name].split('--')[1].split('.')[0]] = correctGT(mypath+'/'+project_dic[name].split('--')[1], dic_aitong)
    elif '实体瘤泛癌种50基因（靶向+化疗+癌痛）' in project_dic[name].split('--')[0] or '实体瘤泛癌种50基因（靶向+化疗)' in project_dic[name].split('--')[0] or '实体瘤泛癌种160基因' in project_dic[name].split('--')[0]:
        gene_50['gene_50'+'__'+name+'--'+project_dic[name].split('--')[1].split('.')[0]] = correctGT(mypath+'/'+project_dic[name].split('--')[1], dic_50gene)
        gene_aitong['gene_aitong'+'__'+name+'--'+project_dic[name].split('--')[1].split('.')[0]] = correctGT(mypath+'/'+project_dic[name].split('--')[1], dic_aitong)
    elif '实体瘤泛癌种500基因' in project_dic[name].split('--')[0] or '实体瘤泛癌种642基因（靶向+免疫+化疗+癌痛+遗传风险）' in project_dic[name].split('--')[0] or '实体瘤泛癌种642基因（靶向+免疫+化疗+癌痛+遗传风险）'in project_dic[name].split('--')[0]:
        gene_500['gene_500'+'__'+name+'--'+project_dic[name].split('--')[1].split('.')[0]] = correctGT(mypath+'/'+project_dic[name].split('--')[1], dic_500gene)
        gene_aitong500['gene_aitong500'+'__'+name+'--'+project_dic[name].split('--')[1].split('.')[0]] = correctGT(mypath+'/'+project_dic[name].split('--')[1], dic_aitong500)
    elif '肺癌21基因（靶向+癌痛）' in project_dic[name].split('--')[0]:
        gene_aitong['gene_aitong'+'__'+name+'--'+project_dic[name].split('--')[1].split('.')[0]] = correctGT(mypath+'/'+project_dic[name].split('--')[1], dic_aitong)
    elif '肠癌37基因' in project_dic[name].split('--')[0]:
        gene_chang37['gene_chang37'+'__'+name+'--'+project_dic[name].split('--')[1].split('.')[0]] = correctGT(mypath+'/'+project_dic[name].split('--')[1], dic_chang37)
        gene_aitong['gene_aitong'+'__'+name+'--'+project_dic[name].split('--')[1].split('.')[0]] = correctGT(mypath+'/'+project_dic[name].split('--')[1], dic_aitong)

    else:
        pass

dic_all = {'gene_37':gene_37, 'gene_50':gene_50, 'gene_500':gene_500, 
'gene_aitong':gene_aitong, 'gene_aitong500':gene_aitong500, 'gene_chang37':gene_chang37 }

#print(gene_aitong)
finall_dic = {}
for cancer_name in dic_all.keys():
    finall_dic.setdefault(cancer_name, {})



############################################################################################################
for key in dic_all.keys():
    if dic_all[key]:
        dic_client = dic_all[key]
        df = pd.read_excel(dic_path[key])
        df = df.dropna(axis = 0, subset = ['类别'] )
        
        def make_column(string):
            a = ''
            list1 = []
            for i in df.index:
                if type(df[string][i]) != type(df[string][2]):
                    a = df[string][i]
                    list1.append(a)
                else:
                    list1.append(a)
            return list1
        
        for i in ['化疗药物', '基因', '位点', '证据等级']:
            df[i] = (make_column(i))
        
        dic = {}
        dic1 = {}
        for i in df.index:
            dic.setdefault(df['化疗药物'][i] + '\t' + df['基因'][i] + '\t' + df['位点'][i], {})
            dic1.setdefault(df['化疗药物'][i] + '\t' + df['基因'][i] + '\t' + df['位点'][i], {})

            dic[df['化疗药物'][i] + '\t' + df['基因'][i] + '\t' + df['位点'][i]][df['基因型'][i]] = df['解释'][i]
            dic1[df['化疗药物'][i] + '\t' + df['基因'][i] + '\t' + df['位点'][i]][df['基因型'][i]] = df['类别'][i]
            dic1[df['化疗药物'][i] + '\t' + df['基因'][i] + '\t' + df['位点'][i]]['证据等级'] = df['证据等级'][i]
    
        level_dic = {'1A':6 , '1B':5, '2A':4, '2B':3, '3':2, '4':1 }
        #输入客户名字，产生临床提示结果
        def clinical_prompt(client_name ):
            d_result = {}#临床提示映射
            list_pinggu = []
            d_test = {}
            dic_aa = {}
            for i in dic1.keys():
                list_pinggu.append(dic1[i][dic_client[client_name][i.split('\t')[2]]] + '--' + str(dic1[i]['证据等级']) )
                dic_pinggu_result = OrderedDict(zip(dic1.keys(), list_pinggu))
            for i in dic_pinggu_result.keys():
                d_test.setdefault(i.split('\t')[0],[])
                d_test[i.split('\t')[0]].append(dic_pinggu_result[i])

            for j, k in d_test.items():
                target = []
                for line in k:
                    for z in line.split('，'):
                        if '--' not in z:
                            target.append(z + '--' + line.split('--')[1])
                        else:
                            target.append(z)
                dic_aa[j] = target
            
            for i, a in dic_aa.items():
                list_effect = []
                
                du = re.findall(r'毒副\w+--\w+', str(a))
                dai = re.findall(r'代谢\w+--\w+', str(a))
                liao = re.findall(r'疗效\w+--\w+', str(a))
                
                top_num_liao = re.findall(r'较好--\w+', str(liao))
                mid_num_liao = re.findall(r'适中--\w+', str(liao))
                bot_num_liao = re.findall(r'较差--\w+', str(liao))
                
                top_num_du = re.findall(r'较高--\w+', str(du))
                mid_num_du = re.findall(r'适中--\w+', str(du))
                bot_num_du = re.findall(r'较低--\w+', str(du))
                
                top_num_dai = re.findall(r'较快--\w+', str(dai))
                mid_num_dai = re.findall(r'适中--\w+', str(dai))
                bot_num_dai = re.findall(r'较慢--\w+', str(dai))
                

                #疗效结果判定
                if len(liao) == 1: #位点数目为1的时候
                    if '适中' in liao[0] and level_dic[liao[0].split('--')[1]] >= level_dic['2A'] or  '较好' in liao[0]:
                        list_effect.append('疗效较好')
                    if '适中' in liao[0] and level_dic[liao[0].split('--')[1]] < level_dic['2A'] or  '较差' in liao[0]:
                        list_effect.append('疗效适中')
                
                if len(liao) == 2:
                    if len(top_num_liao) == 2 or len(top_num_liao ) == 1 and len(mid_num_liao ) == 1:
                        list_effect.append('疗效较好')
                    if len(top_num_liao) == 1 and len(bot_num_liao) == 1 or len(mid_num_liao) == 2 or len(mid_num_liao) == 1 and len(bot_num_liao) == 1 \
                    or len(bot_num_liao) == 2:
                        list_effect.append('疗效适中')
                
                if len(liao) == 3:
                    if len(top_num_liao) == 3 or len(top_num_liao) == 2 and len(mid_num_liao) == 1 or len(top_num_liao) == 2 \
                    and len(bot_num_liao) == 1 or len(top_num_liao) == 1 and len(mid_num_liao) ==2 or len(top_num_liao) == 1 \
                    and len(mid_num_liao) == 1 and len(bot_num_liao) == 1:
                        list_effect.append('疗效较好')
                    if  len(top_num_liao) == 1 and len(bot_num_liao) == 2 or len(mid_num_liao) == 3 or len(mid_num_liao) == 2 \
                    and len(bot_num_liao) == 1 or len(mid_num_liao) == 1 and len(bot_num_liao) == 2 or len(bot_num_liao) == 3:
                        list_effect.append('疗效适中')
                

                        #毒副结果判定
                if i == '氟尿嘧啶+亚叶酸':
                    if set(a) == set(['毒副较低 --1A', '毒副较低--2B', '毒副较高--3']) or set(a) == set(['毒副较低 --1A', '毒副较低--2B', '毒副较低--3']):
                            list_effect.append('毒副较低')
                    
                        
                    if set(a) == set(['毒副较低 --1A', '毒副较高--2B', '毒副较高--3']) or set(a) == set(['毒副较低 --1A', '毒副较高--2B', '毒副较低--3']):
                            list_effect.append('毒副适中')
                
                else:
                    if len(du) == 1:
                        if '较高' in du[0]:
                            list_effect.append('毒副较高')
                        if '适中' in du[0]:
                            list_effect.append('毒副适中')
                        if '较低' in du[0]:
                            list_effect.append('毒副较低')
        
                    if len(du) == 2:    
                        if len(top_num_du) == 2 or len(top_num_du) == 1 and len(mid_num_du) == 1 or len(top_num_du) == 1 and \
                        level_dic[top_num_du[0].split('--')[1]] == level_dic['1A'] and len(bot_num_du) == 1:
                            list_effect.append('毒副较高')
                        if len(top_num_du) == 1 and level_dic[top_num_du[0].split('--')[1]] < level_dic['1A'] and len(bot_num_du) == 1 or len(mid_num_du) \
                        == 2 or len(mid_num_du) == 1 and level_dic[mid_num_du[0].split('--')[1]] >= level_dic['2A'] and len(bot_num_du) \
                        == 1:
                            list_effect.append('毒副适中')
                        if len(mid_num_du) == 1 and level_dic[mid_num_du[0].split('--')[1]] <= level_dic['2B'] and len(bot_num_du) == 1 \
                        or len(bot_num_du) == 2:
                            list_effect.append('毒副较低')
                    
                    if len(du) == 3:
                        if len(top_num_du) == 3 or len(top_num_du) == 2 and len(mid_num_du) == 1 or len(top_num_du) == 1 and len(mid_num_du) \
                        == 2 or len(top_num_du) == len(mid_num_du) == len(bot_num_du) == 1 or len(top_num_du) == 1 and \
                        level_dic[top_num_du[0].split('--')[1]] == level_dic['1A'] and len(bot_num_du) == 2 or len(top_num_du) == 2 \
                        and len(bot_num_du) == 1:
                            list_effect.append('毒副较高')
                        if len(top_num_du) == 1 and level_dic[top_num_du[0].split('--')[1]] < level_dic['1A'] and len(bot_num_du) \
                        == 2 or len(mid_num_du) == 3 or len(mid_num_du) == 2 and len(bot_num_du) == 1 or len(mid_num_du) == 1 \
                        and level_dic[mid_num_du[0].split('--')[1]] == level_dic['1A'] and len(bot_num_du) == 2:
                            list_effect.append('毒副适中')
                        if len(mid_num_du) == 1 and level_dic[mid_num_du[0].split('--')[1]] < level_dic['1A'] and len(bot_num_du) == 2 \
                        or len(bot_num_du) == 3:
                            list_effect.append('毒副较低')
            
                    if len(du) == 4:
                        if set(du) == {'毒副较低--1A','毒副较低--1A','毒副较高--2A','毒副较高--3'} or \
                        set(du) == {'毒副较低--1A','毒副较低--1A','毒副适中--2A','毒副较高--3'}:
                            list_effect.append('毒副适中')
                        if set(du) == {'毒副较低--1A','毒副较低--1A','毒副较高--2A','毒副较低--3'} or \
                        set(du) == {'毒副较低--1A','毒副较低--1A','毒副适中--2A','毒副较低--3'} or \
                        set(du) == {'毒副较低--1A','毒副较低--1A','毒副较低--2A','毒副较高--3'} or \
                        set(du) == {'毒副较低--1A','毒副较低--1A','毒副较低--2A','毒副适中--3'} or \
                        set(du) == {'毒副较低--1A','毒副较低--1A','毒副较低--2A','毒副较低--3'}:
                            list_effect.append('毒副较低')
                
                    if len(du) == 5:
                        if set(du) == {'毒副较低--1A','毒副较低--1A','毒副较高--2A','毒副较高--3','毒副较高--3'} or \
                        set(du) == {'毒副较低--1A','毒副较低--1A','毒副较高--2A','毒副较高--3','毒副适中--3'} or \
                        set(du) == {'毒副较低--1A','毒副较低--1A','毒副较高--2A','毒副较高--3','毒副较低--3'} or \
                        set(du) == {'毒副较低--1A','毒副较低--1A','毒副适中--2A','毒副较高--3','毒副较高--3'}:
                            list_effect.append('毒副适中')
                        else:
                            list_effect.append('毒副较低')

                 #代谢结果判定
                if len(dai) == 1:
                    if '较快' in dai[0]:
                        list_effect.append('代谢较快')
                    if '适中' in dai[0]:
                        list_effect.append('代谢适中')
                    if '较慢' in dai[0]:
                        list_effect.append('代谢较慢')
                
                if len(dai) == 2:
                    if len(top_num_dai) == 2 or len(top_num_dai) == 1 and len(mid_num_dai) == 1:
                        list_effect.append('代谢较快')
                    if len(top_num_dai) == 1 and len(bot_num_dai) == 1 and level_dic[bot_num_dai[0].split('--')[1]] \
                    < level_dic['1A'] or len(mid_num_dai) == 2:
                        list_effect.append('代谢适中')
                    if len(mid_num_dai) == 1 and len(bot_num_dai) == 1 or len(bot_num_dai) == 2 or len(top_num_dai) \
                    == 1 and len(bot_num_dai) == 1 and level_dic[bot_num_dai[0].split('--')[1]] == level_dic['1A']:
                        list_effect.append('代谢较慢')
            
            
                d_result[i] = '，'.join(list_effect)
            return d_result
        
        
        def modify_du(name): #降低白蛋白紫杉醇毒副作用等级
            dic_tem = clinical_prompt(name)
            if '白蛋白紫杉醇' in dic_tem.keys():
                dic_tem['白蛋白紫杉醇'] = dic_tem['白蛋白紫杉醇'].replace('毒副适中','毒副较低').replace('毒副较高', '毒副适中')
            return dic_tem
        

        def gene_type_level(name):
            gene_type_dic = {}
            for i in dic1.keys():
                gene_type_dic.setdefault(i, {})
                gene_type_dic[i]['基因型'] = dic_client[name][i.split('\t')[-1]]
                gene_type_dic[i]['证据等级'] = dic1[i]['证据等级']
                text = dic1[i][dic_client[name][i.split('\t')[2]]]
                dai = re.findall(r'代谢', text)
                du = re.findall(r'毒副', text)
                liao = list(set(re.findall(r'疗效', text)))
                x = []
                for k in [liao, du, dai]:
                    if k:
                        x += k
                gene_type_dic[i]['类别'] = '，'.join(x).replace('副', '性')
            return gene_type_dic
        
        
        
        
        cancer_type = list(dic_client.keys())[0].split('__')[0]#判断癌种
        print(cancer_type)
        for name in dic_client.keys():
            finall_dic[cancer_type].setdefault(name,{})
            finall_dic[cancer_type][name]['临床提示'] = modify_du(name)
            finall_dic[cancer_type][name]['基因型'] = gene_type_level(name)

#for key in finall_dic.keys():
#    if finall_dic[name]:
#        print(cancer_type)
pp = pprint.PrettyPrinter(indent=6)
pp.pprint(finall_dic)
#pprint(finall_dic)
