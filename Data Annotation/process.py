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
            newpath = path + '/' +  f
            for f1 in os.listdir(newpath):
                newpath2 = newpath + '/' +  f1
                for f2 in os.listdir(newpath2):
                    newpath3 = newpath2 + '/' +  f2
                    for file in os.listdir(newpath3):
                        if(type == 'CN'):
                            CN = CN +1
                        elif(type == 'AD'):
                            AD = AD +1
                        elif(type == 'MCI'):
                            MCI = MCI +1

                        T = T +1
                        newpath4 = newpath3 + '/' +  file
                        last_path = des_path + type + '/' + file
                        ds = pydicom.dcmread(newpath4)
                        ds.save_as(last_path)

    print(i+1,"/",l)

print('CN ',CN)
print('AD ',AD)
print('MCI ',MCI)
print('total ',T)

