import pydicom 
import os
import pandas as pd 

des_path_base = './Datas/SEPARATED/'
CN =0
MCI =0
AD=0
T=0
csv_file = pd.read_csv('./Datas/ADNI_MRI_8_18_2023.csv')
length = len(csv_file)
basepath = './Datas/ADNI'
for i in range(length):
    path = basepath + '/' + csv_file.iloc[i]['Subject']
    type =  csv_file.iloc[i]['Group']
    for dir1 in os.listdir(path):
        if dir1!='SURVEY':
            dir_path1 = path + '/' +  dir1
            for dir2 in os.listdir(dir_path1):
                dir_path2 = dir_path1 + '/' +  dir2
                for dir3 in os.listdir(dir_path2):
                    dir_path3 = dir_path2 + '/' +  dir3
                    for file in os.listdir(dir_path3):
                        if(type == 'CN'):
                            CN = CN +1
                        elif(type == 'AD'):
                            AD = AD +1
                        elif(type == 'MCI'):
                            MCI = MCI +1

                        T = T +1
                        source_path = dir_path3 + '/' +  file
                        des_path = des_path_base + type + '/' + file
                        ds = pydicom.dcmread(source_path)
                        ds.save_as(des_path)

    print(i+1,"/",length)

print('CN ',CN)
print('AD ',AD)
print('MCI ',MCI)
print('total ',T)

