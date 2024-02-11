import pydicom 
import os
import pandas as pd 

des_path = './Datas/SEPARATED/'
CN =0
MCI =0
AD=0
T=0
dfile = pd.read_csv('./Datas/ADNI_MRI_8_18_2023.csv')
l = len(dfile)
basepath = './Datas/ADNI'
for i in range(l):
    path = basepath + '/' + dfile.iloc[i]['Subject']
    type =  dfile.iloc[i]['Group']
    for f in os.listdir(path):
        if f!='SURVEY':
            dir_path1 = path + '/' +  f
            for f1 in os.listdir(dir_path1):
                dir_path2 = dir_path1 + '/' +  f1
                for f2 in os.listdir(dir_path2):
                    dir_path3 = dir_path2 + '/' +  f2
                    for file in os.listdir(dir_path3):
                        if(type == 'CN'):
                            CN = CN +1
                        elif(type == 'AD'):
                            AD = AD +1
                        elif(type == 'MCI'):
                            MCI = MCI +1

                        T = T +1
                        dir_path4 = dir_path3 + '/' +  file
                        final_path = des_path + type + '/' + file
                        ds = pydicom.dcmread(dir_path4)
                        ds.save_as(final_path)

    print(i+1,"/",l)

print('CN ',CN)
print('AD ',AD)
print('MCI ',MCI)
print('total ',T)

