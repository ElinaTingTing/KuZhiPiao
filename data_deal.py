# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:35:29 2019

@author: secoo
"""
import os
import pickle
import numpy as np
import pandas as pd 
from pandas import DataFrame as df

<<<<<<< HEAD
pa=os.getcwd()
###---------------存放各个月份的数据--------------------###
file4_path=pa+r'\original_data\4'  ##截至到各个月底的数据，4月份
file5_path=pa+r'\original_data\5'
file6_path=pa+r'\original_data\6'
file7_path=pa+r'\original_data\7'
file8_path=pa+r'\original_data\8'
file9_path=pa+r'\original_data\9'
file10_path=pa+r'\original_data\10'
file11_path=pa+r'\original_data\11'
file12_path=pa+r'\original_data\12'
file1_path=pa+r'\original_data\1'
file2_path=pa+r'\original_data\2'
file3_path=pa+r'\original_data\3'
file42_path=pa+r'\original_data\4_2'
file52_path=pa+r'\original_data\5_2'
file62_path=pa+r'\original_data\6_2'
file72_path=pa+r'\original_data\7_2'
file82_path=pa+r'\original_data\8_2'
file92_path=pa+r'\original_data\9_2'
=======
pa=os.getcwd()+"\\data"
###---------------存放各个月份的数据--------------------###
file4_path=pa+r'\4'  ##截至到各个月底的数据，4月份
file5_path=pa+r'\5'
file6_path=pa+r'\6'
file7_path=pa+r'\7'
file8_path=pa+r'\8'
file9_path=pa+r'\9'
file10_path=pa+r'\10'
file11_path=pa+r'\11'
file12_path=pa+r'\12'
file1_path=pa+r'\1'
file2_path=pa+r'\2'
file3_path=pa+r'\3'  
file42_path=pa+r'\4_2'  
file52_path=pa+r'\5_2'  
file62_path=pa+r'\6_2' 
file72_path=pa+r'\7_2' 
file82_path=pa+r'\8_2'
>>>>>>> 9c0f50775ad9ec9ab7b09b6a8d96d239cdb0911b

## 4月份统计的数据
data4=df()
for file in os.listdir(file4_path):
    data_per=pd.read_excel(file4_path+'\\'+file)
    data4=pd.concat([data4,data_per])
data4=data4.drop_duplicates()
data4=data4[(data4['渠道']!='浦发')&(data4['渠道']!='银联')]
    
## 5月份统计的数据
data5=df()
for file in os.listdir(file5_path):
    data_per=pd.read_excel(file5_path+'\\'+file)
    data5=pd.concat([data5,data_per])
data5=data5.drop_duplicates()
data5=data5[(data5['渠道']!='浦发')&(data5['渠道']!='银联')]    
            
## 6月份统计数据
data6=df()
for file in os.listdir(file6_path):
    data_per=pd.read_excel(file6_path+'\\'+file)
    data6=pd.concat([data6,data_per])
data6=data6.drop_duplicates()
data6=data6[(data6['渠道']!='浦发')&(data6['渠道']!='银联')] 
            
## 7月份统计数据
data7=df()
for file in os.listdir(file7_path):
    data_per=pd.read_excel(file7_path+'\\'+file)
    data7=pd.concat([data7,data_per])
data7=data7.drop_duplicates()
data7=data7[(data7['渠道']!='浦发')&(data7['渠道']!='银联')] 
data7=data7[~data7['渠道'].isnull()]


## 8月份统计数据（截至到8月底）
data8=df()
for file in os.listdir(file8_path):
    print(file)
    data_per=pd.read_excel(file8_path+'\\'+file)
    data8=pd.concat([data8,data_per])
data8=data8.drop_duplicates()
data8=data8[(data8['渠道']!='浦发')&(data8['渠道']!='银联')] 
data8=data8[~data8['渠道'].isnull()]


## 9月份统计数据（截止到9月底）
data9=df()
for file in os.listdir(file9_path):
    print(file)
    data_per=pd.read_excel(file9_path+'\\'+file)
    data9=pd.concat([data9,data_per])
data9=data9.drop_duplicates()
data9=data9[(data9['渠道']!='浦发')&(data9['渠道']!='银联')] 
data9=data9[~data9['渠道'].isnull()]

## 10月份统计数据（截止到10月底）
data10=df()
for file in os.listdir(file10_path):
    print(file)
    data_per=pd.read_excel(file10_path+'\\'+file)
    data10=pd.concat([data10,data_per])
data10=data10.drop_duplicates()
data10=data10[(data10['渠道']!='浦发')&(data10['渠道']!='银联')] 
data10=data10[~data10['渠道'].isnull()]

## 11月份统计数据
data11=df()
for file in os.listdir(file11_path):
    print(file)
    data_per=pd.read_excel(file11_path+'\\'+file)
    data11=pd.concat([data11,data_per])
data11=data11.drop_duplicates()
data11=data11[(data11['渠道']!='浦发')&(data11['渠道']!='银联')] 
data11=data11[~data11['渠道'].isnull()]

## 12月份统计数据
data12=df()
for file in os.listdir(file12_path):
    print(file)
    data_per=pd.read_excel(file12_path+'\\'+file)
    data12=pd.concat([data12,data_per])
data12=data12.drop_duplicates()
data12=data12[(data12['渠道']!='浦发')&(data12['渠道']!='银联')] 
data12=data12[~data12['渠道'].isnull()]

## 2020年1月份统计数据
data1=df()
for file in os.listdir(file1_path):
    print(file)
    data_per=pd.read_excel(file1_path+'\\'+file)
    data1=pd.concat([data1,data_per])
data1=data1.drop_duplicates()
data1=data1[(data1['渠道']!='浦发')&(data1['渠道']!='银联')] 
data1=data1[~data1['渠道'].isnull()]

data2=df()
for file in os.listdir(file2_path):
    try:
        print(file)
        data_per=pd.read_excel(file2_path+'\\'+file)
        data2=pd.concat([data2,data_per])
    except:
        continue     
data2=data2.drop_duplicates()
data2=data2[(data2['渠道']!='浦发')&(data2['渠道']!='银联')] 
data2=data2[~data2['渠道'].isnull()]

data3=df()
for file in os.listdir(file3_path):
    try:
        print(file)
        data_per=pd.read_excel(file3_path+'\\'+file)
        data3=pd.concat([data3,data_per])
    except:
        continue     
data3=data3.drop_duplicates()
data3=data3[(data3['渠道']!='浦发')&(data3['渠道']!='银联')] 
data3=data3[~data3['渠道'].isnull()]

data4_2=df()
for file in os.listdir(file42_path):
    try:
        print(file)
        data_per=pd.read_excel(file42_path+'\\'+file)
        data4_2=pd.concat([data4_2,data_per])
    except:
        continue     
data4_2=data4_2.drop_duplicates()
data4_2=data4_2[(data4_2['渠道']!='浦发')&(data4_2['渠道']!='银联')] 
data4_2=data4_2[~data4_2['渠道'].isnull()]


data5_2=df()
for file in os.listdir(file52_path):
    try:
        print(file)
        data_per=pd.read_excel(file52_path+'\\'+file)
        data5_2=pd.concat([data5_2,data_per])
    except:
        continue     
data5_2=data5_2.drop_duplicates()
data5_2=data5_2[(data5_2['渠道']!='浦发')&(data5_2['渠道']!='银联')] 
data5_2=data5_2[~data5_2['渠道'].isnull()]


data6_2=df()
for file in os.listdir(file62_path):
    try:
        print(file)
        data_per=pd.read_excel(file62_path+'\\'+file)
        data6_2=pd.concat([data6_2,data_per])
    except:
        continue     
data6_2=data6_2.drop_duplicates()
data6_2=data6_2[(data6_2['渠道']!='浦发')&(data6_2['渠道']!='银联')] 
data6_2=data6_2[~data6_2['渠道'].isnull()]


data7_2=df()
for file in os.listdir(file72_path):
    try:
        print(file)
        data_per=pd.read_excel(file72_path+'\\'+file)
        data7_2=pd.concat([data7_2,data_per])
    except:
        continue     
data7_2=data7_2.drop_duplicates()
data7_2=data7_2[(data7_2['渠道']!='浦发')&(data7_2['渠道']!='银联')] 
data7_2=data7_2[~data7_2['渠道'].isnull()]

data8_2=df()
for file in os.listdir(file82_path):
    try:
        print(file)
        data_per=pd.read_excel(file82_path+'\\'+file)
        data8_2=pd.concat([data8_2,data_per])
    except:
        continue     
data8_2=data8_2.drop_duplicates()
data8_2=data8_2[(data8_2['渠道']!='浦发')&(data8_2['渠道']!='银联')] 
data8_2=data8_2[~data8_2['渠道'].isnull()]
<<<<<<< HEAD

data9_2=df()
for file in os.listdir(file92_path):
    try:
        print(file)
        data_per=pd.read_excel(file92_path+'\\'+file)
        data9_2=pd.concat([data9_2,data_per])
    except:
        continue
data9_2=data9_2.drop_duplicates()
data9_2=data9_2[(data9_2['渠道']!='浦发')&(data9_2['渠道']!='银联')]
data9_2=data9_2[~data9_2['渠道'].isnull()]


###-------------------数据存储-----------------------###
# f_=open('data4.pkl','wb')
# pickle.dump(data4,f_)
# f_.close()
# 
# f_=open('data5.pkl','wb')
# pickle.dump(data5,f_)
# f_.close()
# 
# f_=open('data6.pkl','wb')
# pickle.dump(data6,f_)
# f_.close()
# 
# f_=open('data7.pkl','wb')
# pickle.dump(data7,f_)
# f_.close()
# 
# f_=open('data8.pkl','wb')
# pickle.dump(data8,f_)
# f_.close()
# 
# f_=open('data9.pkl','wb')
# pickle.dump(data9,f_)
# f_.close()
# 
# f_=open('data10.pkl','wb')
# pickle.dump(data10,f_)
# f_.close()
# 
# f_=open('data11.pkl','wb')
# pickle.dump(data11,f_)
# f_.close()
# 
# f_=open('data12.pkl','wb')
# pickle.dump(data12,f_)
# f_.close()
# 
# f_=open('data1.pkl','wb')
# pickle.dump(data1,f_)
# f_.close()
# 
# f_=open('data2.pkl','wb')
# pickle.dump(data2,f_)
# f_.close()
# 
# f_=open('data3.pkl','wb')
# pickle.dump(data3,f_)
# f_.close()
# 
# f_=open('data4_2.pkl','wb')
# pickle.dump(data4_2,f_)
# f_.close()
# 
# f_=open('data5_2.pkl','wb')
# pickle.dump(data5_2,f_)
# f_.close()
# 
# f_=open('data6_2.pkl','wb')
# pickle.dump(data6_2,f_)
# f_.close()
# 
# f_=open('data7_2.pkl','wb')
# pickle.dump(data7_2,f_)
# f_.close()
# 
# f_=open('data8_2.pkl','wb')
# pickle.dump(data8_2,f_)
# f_.close()

f_=open('data9_2.pkl','wb')
pickle.dump(data9_2,f_)
f_.close()

###----------------------数据读取----------------------------###
# f_=open('data4.pkl','rb')
# data4=pickle.load(f_)
# f_.close()
# 
# f_=open('data5.pkl','rb')
# data5=pickle.load(f_)
# f_.close()
# 
# f_=open('data6.pkl','rb')
# data6=pickle.load(f_)
# f_.close()
# 
# f_=open('data7.pkl','rb')
# data7=pickle.load(f_)
# f_.close()
# 
# f_=open('data8.pkl','rb')
# data8=pickle.load(f_)
# f_.close()
# 
# f_=open('data9.pkl','rb')
# data9=pickle.load(f_)
# f_.close()
# 
# f_=open('data10.pkl','rb')
# data10=pickle.load(f_)
# f_.close()
# 
# f_=open('data11.pkl','rb')
# data11=pickle.load(f_)
# f_.close()
# 
# f_=open('data12.pkl','rb')
# data12=pickle.load(f_)
# f_.close()
# 
# f_=open('data1.pkl','rb')
# data1=pickle.load(f_)
# f_.close()
# 
# f_=open('data2.pkl','rb')
# data2=pickle.load(f_)
# f_.close()
# 
# f_=open('data3.pkl','rb')
# data3=pickle.load(f_)
# f_.close()
# 
# f_=open('data4_2.pkl','rb')
# data4_2=pickle.load(f_)
# f_.close()
# 
# f_=open('data5_2.pkl','rb')
# data5_2=pickle.load(f_)
# f_.close()
# 
# f_=open('data6_2.pkl','rb')
# data6_2=pickle.load(f_)
# f_.close()
# 
# f_=open('data7_2.pkl','rb')
# data7_2=pickle.load(f_)
# f_.close()
# 
# f_=open('data8_2.pkl','rb')
# data8_2=pickle.load(f_)
# f_.close()

f_=open('data9_2.pkl','rb')
data9_2=pickle.load(f_)
f_.close()


=======
###-------------------数据存储-----------------------###
f_=open('data4.pkl','wb')
pickle.dump(data4,f_)
f_.close()

f_=open('data5.pkl','wb')
pickle.dump(data5,f_)
f_.close()

f_=open('data6.pkl','wb')
pickle.dump(data6,f_)
f_.close()

f_=open('data7.pkl','wb')
pickle.dump(data7,f_)
f_.close()

f_=open('data8.pkl','wb')
pickle.dump(data8,f_)
f_.close()

f_=open('data9.pkl','wb')
pickle.dump(data9,f_)
f_.close()

f_=open('data10.pkl','wb')
pickle.dump(data10,f_)
f_.close()

f_=open('data11.pkl','wb')
pickle.dump(data11,f_)
f_.close()

f_=open('data12.pkl','wb')
pickle.dump(data12,f_)
f_.close()

f_=open('data1.pkl','wb')
pickle.dump(data1,f_)
f_.close()

f_=open('data2.pkl','wb')
pickle.dump(data2,f_)
f_.close()

f_=open('data3.pkl','wb')
pickle.dump(data3,f_)
f_.close()

f_=open('data4_2.pkl','wb')
pickle.dump(data4_2,f_)
f_.close()

f_=open('data5_2.pkl','wb')
pickle.dump(data5_2,f_)
f_.close()

f_=open('data6_2.pkl','wb')
pickle.dump(data6_2,f_)
f_.close()

f_=open('data7_2.pkl','wb')
pickle.dump(data7_2,f_)
f_.close()

f_=open('data8_2.pkl','wb')
pickle.dump(data8_2,f_)
f_.close()

###----------------------数据读取----------------------------###
f_=open('data4.pkl','rb')
data4=pickle.load(f_)
f_.close()

f_=open('data5.pkl','rb')
data5=pickle.load(f_)
f_.close()

f_=open('data6.pkl','rb')
data6=pickle.load(f_)
f_.close()

f_=open('data7.pkl','rb')
data7=pickle.load(f_)
f_.close()

f_=open('data8.pkl','rb')
data8=pickle.load(f_)
f_.close()

f_=open('data9.pkl','rb')
data9=pickle.load(f_)
f_.close()

f_=open('data10.pkl','rb')
data10=pickle.load(f_)
f_.close()

f_=open('data11.pkl','rb')
data11=pickle.load(f_)
f_.close()

f_=open('data12.pkl','rb')
data12=pickle.load(f_)
f_.close()

f_=open('data1.pkl','rb')
data1=pickle.load(f_)
f_.close()

f_=open('data2.pkl','rb')
data2=pickle.load(f_)
f_.close()

f_=open('data3.pkl','rb')
data3=pickle.load(f_)
f_.close()

f_=open('data4_2.pkl','rb')
data4_2=pickle.load(f_)
f_.close()

f_=open('data5_2.pkl','rb')
data5_2=pickle.load(f_)
f_.close()

f_=open('data6_2.pkl','rb')
data6_2=pickle.load(f_)
f_.close()

f_=open('data7_2.pkl','rb')
data7_2=pickle.load(f_)
f_.close()

f_=open('data8_2.pkl','rb')
data8_2=pickle.load(f_)
f_.close()
>>>>>>> 9c0f50775ad9ec9ab7b09b6a8d96d239cdb0911b
###----------------------异常数据--------------------------###
data6['逾期天数'][data6['逾期本金']==0]=0
data7['逾期天数'][data7['逾期本金']==0]=0
data8['逾期天数'][data8['逾期本金']==0]=0
data9['逾期天数'][data9['逾期本金']==0]=0
data10['逾期天数'][data10['逾期本金']==0]=0
data11['逾期天数'][data11['逾期本金']==0]=0
data12['逾期天数'][data12['逾期本金']==0]=0
data1['逾期天数'][data1['逾期本金']==0]=0
data2['逾期天数'][data2['逾期本金']==0]=0
data3['逾期天数'][data3['逾期本金']==0]=0
data4_2['逾期天数'][data4_2['逾期本金']==0]=0
data5_2['逾期天数'][data5_2['逾期本金']==0]=0
data6_2['逾期天数'][data6_2['逾期本金']==0]=0
data7_2['逾期天数'][data7_2['逾期本金']==0]=0
data8_2['逾期天数'][data8_2['逾期本金']==0]=0
<<<<<<< HEAD
data9_2['逾期天数'][data9_2['逾期本金']==0]=0
=======
>>>>>>> 9c0f50775ad9ec9ab7b09b6a8d96d239cdb0911b

###-------------------划分渠道-------------------------###    
data4['渠道1']=data4['渠道'].map({'马上消费':'马上消费','自授信,众安':'众安','众安':'众安',\
     '众安,众安,阳光,阳光':'阳光','众安,阳光,阳光':'阳光','自授信,阳光,阳光':'阳光',\
     '自授信,阳光':'阳光','阳光':'阳光','自授信':'自授信','众安,阳光':'阳光'})
data5['渠道1']=data5['渠道'].map({'马上消费':'马上消费','自授信,众安':'众安',\
     '众安':'众安','自授信,阳光':'阳光','阳光':'阳光','自授信':'自授信','众安,阳光':'阳光'})
data6['渠道1']=data6['渠道'].map({'马上消费':'马上消费','自授信,众安':'众安',\
     '众安':'众安','自授信,阳光':'阳光','阳光':'阳光','自授信':'自授信','众安,阳光':'阳光'})    
data7['渠道1']=data7['渠道'].map({'马上消费':'马上消费','自授信,众安':'众安',\
     '众安':'众安','自授信,阳光':'阳光','阳光':'阳光','自授信':'自授信','众安,阳光':'阳光','京东白条':'京东白条'})    
data8['渠道1']=data8['渠道'].map({'马上消费':'马上消费','自授信,众安':'众安',\
     '众安':'众安','自授信,阳光':'阳光','阳光':'阳光','自授信':'自授信','众安,阳光':'阳光','京东白条':'京东白条'})        
data9['渠道1']=data9['渠道'].map({'马上消费':'马上消费','自授信,众安':'众安',\
     '众安':'众安','自授信,阳光':'阳光','阳光':'阳光','自授信':'自授信','众安,阳光':'阳光','京东白条':'京东白条'})      
data10['渠道1']=data10['渠道'].map({'马上消费':'马上消费','自授信,众安':'众安',\
     '众安':'众安','自授信,阳光':'阳光','阳光':'阳光','自授信':'自授信','众安,阳光':'阳光','京东白条':'京东白条'})          
data11['渠道1']=data11['渠道'].map({'马上消费':'马上消费','自授信,众安':'众安',\
     '众安':'众安','自授信,阳光':'阳光','阳光':'阳光','自授信':'自授信','众安,阳光':'阳光','京东白条':'京东白条'})          
data12['渠道1']=data12['渠道'].map({'马上消费':'马上消费','自授信,众安':'众安',\
 '众安':'众安','自授信,阳光':'阳光','阳光':'阳光','自授信':'自授信','众安,阳光':'阳光','京东白条':'京东白条'})          
data1['渠道1']=data1['渠道'].map({'马上消费':'马上消费','自授信,众安':'众安',\
 '众安':'众安','自授信,阳光':'阳光','阳光':'阳光','自授信':'自授信','众安,阳光':'阳光','京东白条':'京东白条'})          

data2['渠道1']=data2['渠道'].map({'马上消费':'马上消费','自授信,众安':'众安',\
 '众安':'众安','自授信,阳光':'阳光','阳光':'阳光','自授信':'自授信','众安,阳光':'阳光','京东白条':'京东白条'})          

data3['渠道1']=data3['渠道'].map({'马上消费':'马上消费','自授信,众安':'众安',\
 '众安':'众安','自授信,阳光':'阳光','阳光':'阳光','自授信':'自授信','众安,阳光':'阳光','京东白条':'京东白条'})          
    
data4_2['渠道1']=data4_2['渠道'].map({'马上消费':'马上消费','自授信,众安':'众安',\
 '众安':'众安','自授信,阳光':'阳光','阳光':'阳光','自授信':'自授信','众安,阳光':'阳光','京东白条':'京东白条'})    
  
data5_2['渠道1']=data5_2['渠道'].map({'马上消费':'马上消费','自授信,众安':'众安',\
 '众安':'众安','自授信,阳光':'阳光','阳光':'阳光','自授信':'自授信','众安,阳光':'阳光','京东白条':'京东白条'})    
    
data6_2['渠道1']=data6_2['渠道'].map({'马上消费':'马上消费','自授信,众安':'众安',\
 '众安':'众安','自授信,阳光':'阳光','阳光':'阳光','自授信':'自授信','众安,阳光':'阳光','京东白条':'京东白条'})    

data7_2['渠道1']=data7_2['渠道'].map({'马上消费':'马上消费','自授信,众安':'众安',\
 '众安':'众安','自授信,阳光':'阳光','阳光':'阳光','自授信':'自授信','众安,阳光':'阳光','京东白条':'京东白条'})    

data8_2['渠道1']=data8_2['渠道'].map({'马上消费':'马上消费','自授信,众安':'众安',\
<<<<<<< HEAD
 '众安':'众安','自授信,阳光':'阳光','阳光':'阳光','自授信':'自授信','众安,阳光':'阳光','京东白条':'京东白条'})

data9_2['渠道1']=data9_2['渠道'].map({'马上消费':'马上消费','自授信,众安':'众安',\
 '众安':'众安','自授信,阳光':'阳光','阳光':'阳光','自授信':'自授信','众安,阳光':'阳光','京东白条':'京东白条'})
=======
 '众安':'众安','自授信,阳光':'阳光','阳光':'阳光','自授信':'自授信','众安,阳光':'阳光','京东白条':'京东白条'})    
>>>>>>> 9c0f50775ad9ec9ab7b09b6a8d96d239cdb0911b
    
data4['逾期天数']=data4['逾期天数'].fillna(0)    
data5['逾期天数']=data5['逾期天数'].fillna(0)  
data6['逾期天数']=data6['逾期天数'].fillna(0) 
data7['逾期天数']=data7['逾期天数'].fillna(0)    
data8['逾期天数']=data8['逾期天数'].fillna(0)    
data9['逾期天数']=data9['逾期天数'].fillna(0)    
data10['逾期天数']=data10['逾期天数'].fillna(0)    
data11['逾期天数']=data11['逾期天数'].fillna(0)    
data12['逾期天数']=data12['逾期天数'].fillna(0)      
data1['逾期天数']=data1['逾期天数'].fillna(0)    
data2['逾期天数']=data2['逾期天数'].fillna(0)   
data3['逾期天数']=data3['逾期天数'].fillna(0)     
data4_2['逾期天数']=data4_2['逾期天数'].fillna(0)    
data5_2['逾期天数']=data5_2['逾期天数'].fillna(0)  
data6_2['逾期天数']=data6_2['逾期天数'].fillna(0)  
data7_2['逾期天数']=data7_2['逾期天数'].fillna(0)  
<<<<<<< HEAD
data8_2['逾期天数']=data8_2['逾期天数'].fillna(0)
data9_2['逾期天数']=data9_2['逾期天数'].fillna(0)  
=======
data8_2['逾期天数']=data8_2['逾期天数'].fillna(0)  
>>>>>>> 9c0f50775ad9ec9ab7b09b6a8d96d239cdb0911b

data4['授信时间']=pd.to_datetime(data4['授信时间'].apply(lambda x:x.split(' ')[0]))
data5['授信时间']=pd.to_datetime(data5['授信时间'].apply(lambda x:x.split(' ')[0]))
data6['授信时间']=pd.to_datetime(data6['授信时间'].apply(lambda x:x.split(' ')[0]))
data7['授信时间']=pd.to_datetime(data7['授信时间'].apply(lambda x:x.split(' ')[0]))
data8['授信时间']=pd.to_datetime(data8['授信时间'].apply(lambda x:x.split(' ')[0]))
data9['授信时间']=pd.to_datetime(data9['授信时间'].apply(lambda x:x.split(' ')[0]))
data10['授信时间']=pd.to_datetime(data10['授信时间'].apply(lambda x:x.split(' ')[0]))
data10=data10[~(data10['授信时间']>'2019-10-31')]
data11['授信时间']=pd.to_datetime(data11['授信时间'].apply(lambda x:x.split(' ')[0]))
data11=data11[~(data11['授信时间']>'2019-11-30')] 
data12['授信时间']=pd.to_datetime(data12['授信时间'].apply(lambda x:x.split(' ')[0]))
data12=data12[~(data12['授信时间']>'2019-12-31')] 
data1['授信时间']=pd.to_datetime(data1['授信时间'].apply(lambda x:x.split(' ')[0]))
data1=data1[~(data1['授信时间']>'2020-01-31')] 
data2['授信时间']=pd.to_datetime(data2['授信时间'].apply(lambda x:x.split(' ')[0]))
data2=data2[~(data2['授信时间']>'2020-02-29')] 
data3['授信时间']=pd.to_datetime(data3['授信时间'].apply(lambda x:x.split(' ')[0]))
data3=data3[~(data3['授信时间']>'2020-03-31')] 
data4_2['授信时间']=pd.to_datetime(data4_2['授信时间'].apply(lambda x:x.split(' ')[0]))
data4_2=data4_2[~(data4_2['授信时间']>'2020-04-30')]   
data5_2['授信时间']=pd.to_datetime(data5_2['授信时间'].apply(lambda x:x.split(' ')[0]))
data5_2=data5_2[~(data5_2['授信时间']>'2020-05-31')]   
data6_2['授信时间']=pd.to_datetime(data6_2['授信时间'].apply(lambda x:x.split(' ')[0]))
data6_2=data6_2[~(data6_2['授信时间']>'2020-06-30')]   
data7_2['授信时间']=pd.to_datetime(data7_2['授信时间'].apply(lambda x:x.split(' ')[0]))
data7_2=data7_2[~(data7_2['授信时间']>'2020-07-31')]   
data8_2['授信时间']=pd.to_datetime(data8_2['授信时间'].apply(lambda x:x.split(' ')[0]))
data8_2=data8_2[~(data8_2['授信时间']>'2020-08-31')]
<<<<<<< HEAD
data9_2['授信时间']=pd.to_datetime(data9_2['授信时间'].apply(lambda x:x.split(' ')[0]))
data9_2=data9_2[~(data9_2['授信时间']>'2020-08-31')]
=======

>>>>>>> 9c0f50775ad9ec9ab7b09b6a8d96d239cdb0911b
####调整2月份数据，由于其
#data2["逾期天数"]=np.where((data2["逾期天数"]-25)>0,data2["逾期天数"]-25,0)
#data2["逾期天数"]=np.where(data2["逾期天数"]<20,0,data2["逾期天数"])

##----------剔除京东白条数据-----------------##
data4=data4[data4["渠道1"]!="京东白条"]
data4.index=range(len(data4))
data5=data5[data5["渠道1"]!="京东白条"]
data5.index=range(len(data5))
data6=data6[data6["渠道1"]!="京东白条"]
data6.index=range(len(data6))
data7=data7[data7["渠道1"]!="京东白条"]
data7.index=range(len(data7))
data8=data8[data8["渠道1"]!="京东白条"]
data8.index=range(len(data8))
data9=data9[data9["渠道1"]!="京东白条"]
data9.index=range(len(data9))
data10=data10[data10["渠道1"]!="京东白条"]
data10.index=range(len(data10))
data11=data11[data11["渠道1"]!="京东白条"]
data11.index=range(len(data11))
data12=data12[data12["渠道1"]!="京东白条"]
data12.index=range(len(data12))
data1=data1[data1["渠道1"]!="京东白条"]
data1.index=range(len(data1))
data2=data2[data2["渠道1"]!="京东白条"]
data2.index=range(len(data2))
data3=data3[data3["渠道1"]!="京东白条"]
data3.index=range(len(data3))
data4_2=data4_2[data4_2["渠道1"]!="京东白条"]
data4_2.index=range(len(data4_2))
data5_2=data5_2[data5_2["渠道1"]!="京东白条"]
data5_2.index=range(len(data5_2))
data6_2=data6_2[data6_2["渠道1"]!="京东白条"]
data6_2.index=range(len(data6_2))
data7_2=data7_2[data7_2["渠道1"]!="京东白条"]
data7_2.index=range(len(data7_2))
data8_2=data8_2[data8_2["渠道1"]!="京东白条"]
data8_2.index=range(len(data8_2))
<<<<<<< HEAD
data9_2=data9_2[data9_2["渠道1"]!="京东白条"]
data9_2.index=range(len(data9_2))

'-----------需要统计的月份数据-------'
data=data9_2.copy()
=======

'-----------需要统计的月份数据-------'
data=data8_2.copy()
>>>>>>> 9c0f50775ad9ec9ab7b09b6a8d96d239cdb0911b

'--------------- 统计数据--------------'
'----------汇总-------------'
data_shiyong=data[data['累计订单金额']>0]

## 授信使用人数
data.shape[0]
data_shiyong.shape[0]


## 额度使用情况
data['账户信用额度'].sum()
data['账户信用额度'].mean() 

## 授信额度使用比率
data_shiyong['账户信用额度'].sum()
data_shiyong['账户已用额度'].sum()


## 活跃用户
data.groupby('活跃').count()['渠道']

## 逾期金额
a1=data[data['逾期天数']>0]['逾期本金'].sum() 
a2=data[(data['逾期天数']<=30)&(data['逾期天数']>0)]['逾期本金'].sum() 
a3=data[(data['逾期天数']<=60)&(data['逾期天数']>30)]['逾期本金'].sum() 
a4=data[(data['逾期天数']<=90)&(data['逾期天数']>60)]['逾期本金'].sum()  
a5=data[(data['逾期天数']>90)]['逾期本金'].sum() 
data['累计订单金额'].sum() 
[a1,a2,a3,a4,a5]

'------------分渠道---------'
data8_shiyong=data8[data8['累计订单金额']>0]
data9_shiyong=data9[data9['累计订单金额']>0]
data10_shiyong=data10[data10['累计订单金额']>0]

## 授信人数
data8.groupby('渠道1').count()['分期']
data8_shiyong.groupby('渠道1').count()['分期']

data9.groupby('渠道1').count()['分期']
data9_shiyong.groupby('渠道1').count()['分期']

data10.groupby('渠道1').count()['分期']
data10_shiyong.groupby('渠道1').count()['分期']


data8.groupby('渠道2').count()['分期']
data8_shiyong.groupby('渠道2').count()['分期']

data9.groupby('渠道2').count()['分期']
data9_shiyong.groupby('渠道2').count()['分期']

data10.groupby('渠道2').count()['分期']
data10_shiyong.groupby('渠道2').count()['分期']

## 授信金额
a1=data8_shiyong.groupby('渠道1')['账户信用额度'].sum()
a2=data9_shiyong.groupby('渠道1')['账户信用额度'].sum()
a3=data10_shiyong.groupby('渠道1')['账户信用额度'].sum()
a4=data8_shiyong.groupby('渠道1')['账户已用额度'].sum()
a5=data9_shiyong.groupby('渠道1')['账户已用额度'].sum()
a6=data10_shiyong.groupby('渠道1')['账户已用额度'].sum()
a=pd.concat([a1,a2,a3,a4,a5],axis=1)

##客户活跃情况
data7.pivot_table('分期',index='渠道1',columns='活跃',aggfunc='count')
data8.pivot_table('分期',index='渠道1',columns='活跃',aggfunc='count')
data9.pivot_table('分期',index='渠道1',columns='活跃',aggfunc='count')

data7.pivot_table('分期',index='渠道2',columns='活跃',aggfunc='count')
data8.pivot_table('分期',index='渠道2',columns='活跃',aggfunc='count')
data9.pivot_table('分期',index='渠道2',columns='活跃',aggfunc='count')


   
## 逾期金额
a1=data11[data11['逾期天数']>0].groupby('渠道1')['逾期本金'].sum() 
a2=data11[(data11['逾期天数']<=30)&(data11['逾期天数']>0)].groupby('渠道1')['逾期本金'].sum() 
a3=data11[(data11['逾期天数']<=60)&(data11['逾期天数']>30)].groupby('渠道1')['逾期本金'].sum() 
a4=data11[(data11['逾期天数']<=90)&(data11['逾期天数']>60)].groupby('渠道1')['逾期本金'].sum()  
a5=data11[(data11['逾期天数']>90)].groupby('渠道1')['逾期本金'].sum() 
a6=data11[data11['累计订单金额']>0].groupby('渠道1')['累计订单金额'].sum()  
ss=pd.concat([a1,a2,a3,a4,a5,a6],axis=1)


'------------分月份---------'
data['年份']=data['授信时间'].apply(lambda x:x.year)
data['月份']=data['授信时间'].apply(lambda x:x.month)
data['年月']=data['授信时间'].apply(lambda x:str(x.year)+'-'+str(x.month))
from dateutil import parser
def so(data,col,fun):
    if fun=='count':
        a=df(data.groupby('年月').count()[col])
    elif fun=='mean':
        a=df(data.groupby('年月')[col].mean())
    else:
        a=df(data.groupby('年月')[col].sum())
    a['time']=[parser.parse(i) for i in a.index]
    a=a.sort_values('time')
    a=a[col]
    return a

data_shiyong=data[data['累计订单金额']>0].sort_values(by=['年份','月份'])
#data_shiyong1=data_shiyong[data_shiyong['活跃']=="活跃"]
#data_shiyong2=data[data['账户已用额度']>0].sort_values(by=['年份','月份'])

## 授信人数  
a=so(data,'分期','count')
b=so(data_shiyong,'分期','count')  
a1=pd.concat([a,b],axis=1).fillna(0)
a1['time']=[parser.parse(i) for i in a1.index]
a1=a1.sort_values('time')


## 授信使用额度
a=so(data_shiyong,'账户已用额度','sum')
b=so(data_shiyong,'账户信用额度','sum')  
a1=pd.concat([a,b],axis=1).fillna(0)
a1['time']=[parser.parse(i) for i in a1.index]
a1=a1.sort_values('time')  

## 活跃人数
def so1(data,col,fun):
    a=data.pivot_table('账户已用额度',index='年月',columns=col,aggfunc=fun)
    a['time']=[parser.parse(i) for i in a.index]
    a=a.sort_values('time')
    return a

a=so1(data,'活跃','count').fillna(0)

   
## 逾期金额
a1=so(data[data['逾期天数']>0],'逾期本金','sum')
a2=so(data[(data['逾期天数']<=30)&(data['逾期天数']>0)],'逾期本金','sum')
a3=so(data[(data['逾期天数']<=60)&(data['逾期天数']>30)],'逾期本金','sum')
a4=so(data[(data['逾期天数']<=90)&(data['逾期天数']>60)],'逾期本金','sum')
a5=so(data[(data['逾期天数']>90)],'逾期本金','sum')


a=pd.concat([a1,a2,a3,a4,a5],axis=1).fillna(0)
a5=so(data[data['累计订单金额']>0],'累计订单金额','sum')
a=pd.concat([a,a5],axis=1).fillna(0)
a['time']=[parser.parse(i) for i in a.index]
a=a.sort_values('time')


'--------------资产质量-----------------'
def so11(data,index,columns,value,fun):
    a=data.pivot_table(value,index=index,columns=columns,aggfunc=fun)
    a['time']=[parser.parse(i) for i in a.index]
    a=a.sort_values('time')
    return a

a1=so11(data[data['逾期天数']>0],'年月','渠道1','逾期本金','sum').fillna(0)
b1=so11(data,'年月','渠道1','累计订单金额','sum').fillna(0)


'-------------Vintage---------------'
data4['年月']=data4['授信时间'].apply(lambda x:str(x.year)+'-'+str(x.month))
data5['年月']=data5['授信时间'].apply(lambda x:str(x.year)+'-'+str(x.month))
data6['年月']=data6['授信时间'].apply(lambda x:str(x.year)+'-'+str(x.month))
data7['年月']=data7['授信时间'].apply(lambda x:str(x.year)+'-'+str(x.month))
data8['年月']=data8['授信时间'].apply(lambda x:str(x.year)+'-'+str(x.month))
data9['年月']=data9['授信时间'].apply(lambda x:str(x.year)+'-'+str(x.month))
data10['年月']=data10['授信时间'].apply(lambda x:str(x.year)+'-'+str(x.month))
data11['年月']=data11['授信时间'].apply(lambda x:str(x.year)+'-'+str(x.month))
data12['年月']=data12['授信时间'].apply(lambda x:str(x.year)+'-'+str(x.month))
data1['年月']=data1['授信时间'].apply(lambda x:str(x.year)+'-'+str(x.month))
data2['年月']=data2['授信时间'].apply(lambda x:str(x.year)+'-'+str(x.month))
data3['年月']=data3['授信时间'].apply(lambda x:str(x.year)+'-'+str(x.month))
data4_2['年月']=data4_2['授信时间'].apply(lambda x:str(x.year)+'-'+str(x.month))
data5_2['年月']=data5_2['授信时间'].apply(lambda x:str(x.year)+'-'+str(x.month))
data6_2['年月']=data6_2['授信时间'].apply(lambda x:str(x.year)+'-'+str(x.month))
data7_2['年月']=data7_2['授信时间'].apply(lambda x:str(x.year)+'-'+str(x.month))
data8_2['年月']=data8_2['授信时间'].apply(lambda x:str(x.year)+'-'+str(x.month))


def months(str1,str2):
    year1=int(str1.split('-')[0])
    year2=int(str2.split('-')[0])
    month1=int(str1.split('-')[1])
    month2=int(str2.split('-')[1])
    num=(year1-year2)*12+(month1-month2)
    return num

from dateutil import parser

## Vintage30+
## 人数
def cal(data,long,time): 
    a=data.groupby('年月')['分期'].count()
    yuqi=data[data['逾期天数']>=long].groupby('年月')['分期'].count()
    overdue_rate=df((yuqi/a).fillna(0))
    overdue_rate['time']=[parser.parse(i) for i in overdue_rate.index]
    overdue_rate=overdue_rate.sort_values('time')
    
    result=df(np.zeros((len(a),60)));result.index=overdue_rate.index
    for i in overdue_rate.index:
        month=months(time,i)
        if month>=1:
            result.loc[i,month-1]=overdue_rate.loc[i,'分期']
    return result


#data6=data6[(data6["累计订单金额"]>0)] 
#data7=data7[(data7["累计订单金额"]>0)]   
#data8=data8[(data8["累计订单金额"]>0)]  
#data9=data9[(data9["累计订单金额"]>0)]  
#data10=data10[(data10["累计订单金额"]>0)]  
#data11=data11[(data11["累计订单金额"]>0)]  
#data12=data12[(data12["累计订单金额"]>0)]  
#data1=data1[(data1["累计订单金额"]>0)]   
#data2=data2[(data2["累计订单金额"]>0)]  
#data3=data3[(data3["累计订单金额"]>0)]    

a1=cal(data4,30,'2019-4-30')   
a2=cal(data5,30,'2019-5-31')
a3=cal(data6,30,'2019-6-30')
a4=cal(data7,30,'2019-7-31')
a5=cal(data8,30,'2019-8-31')
a6=cal(data9,30,'2019-9-30')
a7=cal(data10,30,'2019-10-31')
a8=cal(data11,30,'2019-11-30')
a9=cal(data12,30,'2019-12-31')
a10=cal(data1,30,'2020-1-31')
a11=cal(data2,30,'2020-2-29')
a12=cal(data3,30,'2020-3-31')
a13=cal(data4_2,30,'2020-4-30')
a14=cal(data5_2,30,'2020-5-31')
a15=cal(data6_2,30,'2020-6-30')
a16=cal(data7_2,30,'2020-7-31')
a17=cal(data8_2,30,'2020-8-31')


a1.ix['2019-5']=0
a1.ix['2019-6']=0
a1.ix['2019-7']=0
a1.ix['2019-8']=0
a1.ix['2019-9']=0
a1.ix['2019-10']=0
a1.ix['2019-11']=0
a1.ix['2019-12']=0
a1.ix['2020-1']=0
a1.ix['2020-2']=0
a1.ix['2020-3']=0
a1.ix['2020-4']=0
a1.ix['2020-5']=0
a1.ix['2020-6']=0
a1.ix['2020-7']=0

a2.ix['2019-6']=0
a2.ix['2019-7']=0
a2.ix['2019-8']=0
a2.ix['2019-9']=0
a2.ix['2019-10']=0
a2.ix['2019-11']=0
a2.ix['2019-12']=0
a2.ix['2020-1']=0
a2.ix['2020-2']=0
a2.ix['2020-3']=0
a2.ix['2020-4']=0
a2.ix['2020-5']=0
a2.ix['2020-6']=0
a2.ix['2020-7']=0

a3.ix['2019-7']=0
a3.ix['2019-8']=0
a3.ix['2019-9']=0
a3.ix['2019-10']=0
a3.ix['2019-11']=0
a3.ix['2019-12']=0
a3.ix['2020-1']=0
a3.ix['2020-2']=0
a3.ix['2020-3']=0
a3.ix['2020-4']=0
a3.ix['2020-5']=0
a3.ix['2020-6']=0
a3.ix['2020-7']=0

a4.ix['2019-8']=0
a4.ix['2019-9']=0
a4.ix['2019-10']=0
a4.ix['2019-11']=0
a4.ix['2019-12']=0
a4.ix['2020-1']=0
a4.ix['2020-2']=0
a4.ix['2020-3']=0
a4.ix['2020-4']=0
a4.ix['2020-5']=0
a4.ix['2020-6']=0
a4.ix['2020-7']=0

a5.ix['2019-9']=0
a5.ix['2019-10']=0
a5.ix['2019-11']=0
a5.ix['2019-12']=0
a5.ix['2020-1']=0
a5.ix['2020-2']=0
a5.ix['2020-3']=0
a5.ix['2020-4']=0
a5.ix['2020-5']=0
a5.ix['2020-6']=0
a5.ix['2020-7']=0

a6.ix['2019-10']=0
a6.ix['2019-11']=0
a6.ix['2019-12']=0
a6.ix['2020-1']=0
a6.ix['2020-2']=0
a6.ix['2020-3']=0
a6.ix['2020-4']=0
a6.ix['2020-5']=0
a6.ix['2020-6']=0
a6.ix['2020-7']=0

a7.ix['2019-11']=0
a7.ix['2019-12']=0
a7.ix['2020-1']=0
a7.ix['2020-2']=0
a7.ix['2020-3']=0
a7.ix['2020-4']=0
a7.ix['2020-5']=0
a7.ix['2020-6']=0
a7.ix['2020-7']=0

a8.ix['2019-12']=0
a8.ix['2020-1']=0
a8.ix['2020-2']=0
a8.ix['2020-3']=0
a8.ix['2020-4']=0
a8.ix['2020-5']=0
a8.ix['2020-6']=0
a8.ix['2020-7']=0

a9.ix['2020-1']=0
a9.ix['2020-2']=0
a9.ix['2020-3']=0
a9.ix['2020-4']=0
a9.ix['2020-5']=0
a9.ix['2020-6']=0
a9.ix['2020-7']=0

a10.ix['2020-2']=0
a10.ix['2020-3']=0
a10.ix['2020-4']=0
a10.ix['2020-5']=0
a10.ix['2020-6']=0
a10.ix['2020-7']=0

a11.ix['2020-3']=0
a11.ix['2020-4']=0
a11.ix['2020-5']=0
a11.ix['2020-6']=0
a11.ix['2020-7']=0

a12.ix['2020-4']=0
a12.ix['2020-5']=0
a12.ix['2020-6']=0
a12.ix['2020-7']=0


a13.ix['2020-5']=0
a13.ix['2020-6']=0
a13.ix['2020-7']=0

a14.ix['2020-6']=0
a14.ix['2020-7']=0

a15.ix['2020-7']=0

a=a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15+a16

a['time']=[parser.parse(i) for i in a.index]
a=a.sort_values('time')
a=a.drop('time',axis=1)
j=0;mo=abs(months('2019-4-30',"2020-7-31"))+1##应该有数据的月份的个数
for i in a.index:
    month=months('2019-4-30',i)
    if month>=1:
        a.iloc[j,0:month-1]=np.nan
        a.iloc[j,month+(mo-1):45]='-'
    a.iloc[j,month+(mo-1):45]='-'    
    j+=1

j=0
for i in a.index:    
    w=months("2020-2",i)
    if w>0:
        a.iloc[j,w-1]="-"
        j+=1
          
a.to_excel('Vintage30+.xlsx')
 

##Vintage60+
a1=cal(data4,60,'2019-4-30')   
a2=cal(data5,60,'2019-5-31')
a3=cal(data6,60,'2019-6-30')
a4=cal(data7,60,'2019-7-31')
a5=cal(data8,60,'2019-8-31')
a6=cal(data9,60,'2019-9-30')
a7=cal(data10,60,'2019-10-31')
a8=cal(data11,60,'2019-11-30')
a9=cal(data12,60,'2019-12-31')
a10=cal(data1,60,'2020-1-31')
a11=cal(data2,60,'2020-2-29')
a12=cal(data3,60,'2020-3-31')
a13=cal(data4_2,60,'2020-4-30')
a14=cal(data5_2,60,'2020-5-31')
a15=cal(data6_2,60,'2020-6-30')
a16=cal(data7_2,60,'2020-7-31')
a17=cal(data8_2,60,'2020-8-31')

a1.ix['2019-5']=0
a1.ix['2019-6']=0
a1.ix['2019-7']=0
a1.ix['2019-8']=0
a1.ix['2019-9']=0
a1.ix['2019-10']=0
a1.ix['2019-11']=0
a1.ix['2019-12']=0
a1.ix['2020-1']=0
a1.ix['2020-2']=0
a1.ix['2020-3']=0
a1.ix['2020-4']=0
a1.ix['2020-5']=0
a1.ix['2020-6']=0
a1.ix['2020-7']=0

a2.ix['2019-6']=0
a2.ix['2019-7']=0
a2.ix['2019-8']=0
a2.ix['2019-9']=0
a2.ix['2019-10']=0
a2.ix['2019-11']=0
a2.ix['2019-12']=0
a2.ix['2020-1']=0
a2.ix['2020-2']=0
a2.ix['2020-3']=0
a2.ix['2020-4']=0
a2.ix['2020-5']=0
a2.ix['2020-6']=0
a2.ix['2020-7']=0

a3.ix['2019-7']=0
a3.ix['2019-8']=0
a3.ix['2019-9']=0
a3.ix['2019-10']=0
a3.ix['2019-11']=0
a3.ix['2019-12']=0
a3.ix['2020-1']=0
a3.ix['2020-2']=0
a3.ix['2020-3']=0
a3.ix['2020-4']=0
a3.ix['2020-5']=0
a3.ix['2020-6']=0
a3.ix['2020-7']=0

a4.ix['2019-8']=0
a4.ix['2019-9']=0
a4.ix['2019-10']=0
a4.ix['2019-11']=0
a4.ix['2019-12']=0
a4.ix['2020-1']=0
a4.ix['2020-2']=0
a4.ix['2020-3']=0
a4.ix['2020-4']=0
a4.ix['2020-5']=0
a4.ix['2020-6']=0
a4.ix['2020-7']=0

a5.ix['2019-9']=0
a5.ix['2019-10']=0
a5.ix['2019-11']=0
a5.ix['2019-12']=0
a5.ix['2020-1']=0
a5.ix['2020-2']=0
a5.ix['2020-3']=0
a5.ix['2020-4']=0
a5.ix['2020-5']=0
a5.ix['2020-6']=0
a5.ix['2020-7']=0

a6.ix['2019-10']=0
a6.ix['2019-11']=0
a6.ix['2019-12']=0
a6.ix['2020-1']=0
a6.ix['2020-2']=0
a6.ix['2020-3']=0
a6.ix['2020-4']=0
a6.ix['2020-5']=0
a6.ix['2020-6']=0
a6.ix['2020-7']=0

a7.ix['2019-11']=0
a7.ix['2019-12']=0
a7.ix['2020-1']=0
a7.ix['2020-2']=0
a7.ix['2020-3']=0
a7.ix['2020-4']=0
a7.ix['2020-5']=0
a7.ix['2020-6']=0
a7.ix['2020-7']=0

a8.ix['2019-12']=0
a8.ix['2020-1']=0
a8.ix['2020-2']=0
a8.ix['2020-3']=0
a8.ix['2020-4']=0
a8.ix['2020-5']=0
a8.ix['2020-6']=0
a8.ix['2020-7']=0

a9.ix['2020-1']=0
a9.ix['2020-2']=0
a9.ix['2020-3']=0
a9.ix['2020-4']=0
a9.ix['2020-5']=0
a9.ix['2020-6']=0
a9.ix['2020-7']=0

a10.ix['2020-2']=0
a10.ix['2020-3']=0
a10.ix['2020-4']=0
a10.ix['2020-5']=0
a10.ix['2020-6']=0
a10.ix['2020-7']=0

a11.ix['2020-3']=0
a11.ix['2020-4']=0
a11.ix['2020-5']=0
a11.ix['2020-6']=0
a11.ix['2020-7']=0

a12.ix['2020-4']=0
a12.ix['2020-5']=0
a12.ix['2020-6']=0
a12.ix['2020-7']=0

a13.ix['2020-5']=0
a13.ix['2020-6']=0
a13.ix['2020-7']=0

a14.ix['2020-6']=0
a14.ix['2020-7']=0

a15.ix['2020-7']=0

a=a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15+a16

a['time']=[parser.parse(i) for i in a.index]
a=a.sort_values('time')
a=a.drop('time',axis=1)

j=0
for i in a.index:
    month=months('2019-4-30',i)
    if month>=1:
        a.iloc[j,0:month-1]=np.nan
        a.iloc[j,month+(mo-1):45]='-'
    a.iloc[j,month+(mo-1):45]='-'    
    j+=1
    
    
j=0
for i in a.index:    
    w=months("2020-2",i)
    if w>0:
        a.iloc[j,w-1]="-"
        j+=1
          
a.to_excel('Vintage60+.xlsx')



##Vintage90+
a1=cal(data4,90,'2019-4-30')   
a2=cal(data5,90,'2019-5-31')
a3=cal(data6,90,'2019-6-30')
a4=cal(data7,90,'2019-7-31')
a5=cal(data8,90,'2019-8-31')
a6=cal(data9,90,'2019-9-30')
a7=cal(data10,90,'2019-10-31')
a8=cal(data11,90,'2019-11-30')
a9=cal(data12,90,'2019-12-30')
a10=cal(data1,90,'2020-1-31')
a11=cal(data2,90,'2020-2-29')
a12=cal(data3,90,'2020-3-31')
a13=cal(data4_2,90,'2020-4-30')
a14=cal(data5_2,90,'2020-5-31')
a15=cal(data6_2,90,'2020-6-30')
a16=cal(data7_2,90,'2020-7-31')
a17=cal(data8_2,90,'2020-8-31')

a1.ix['2019-5']=0
a1.ix['2019-6']=0
a1.ix['2019-7']=0
a1.ix['2019-8']=0
a1.ix['2019-9']=0
a1.ix['2019-10']=0
a1.ix['2019-11']=0
a1.ix['2019-12']=0
a1.ix['2020-1']=0
a1.ix['2020-2']=0
a1.ix['2020-3']=0
a1.ix['2020-4']=0
a1.ix['2020-5']=0
a1.ix['2020-6']=0
a1.ix['2020-7']=0

a2.ix['2019-6']=0
a2.ix['2019-7']=0
a2.ix['2019-8']=0
a2.ix['2019-9']=0
a2.ix['2019-10']=0
a2.ix['2019-11']=0
a2.ix['2019-12']=0
a2.ix['2020-1']=0
a2.ix['2020-2']=0
a2.ix['2020-3']=0
a2.ix['2020-4']=0
a2.ix['2020-5']=0
a2.ix['2020-6']=0
a2.ix['2020-7']=0


a3.ix['2019-7']=0
a3.ix['2019-8']=0
a3.ix['2019-9']=0
a3.ix['2019-10']=0
a3.ix['2019-11']=0
a3.ix['2019-12']=0
a3.ix['2020-1']=0
a3.ix['2020-2']=0
a3.ix['2020-3']=0
a3.ix['2020-4']=0
a3.ix['2020-5']=0
a3.ix['2020-6']=0
a3.ix['2020-7']=0

a4.ix['2019-8']=0
a4.ix['2019-9']=0
a4.ix['2019-10']=0
a4.ix['2019-11']=0
a4.ix['2019-12']=0
a4.ix['2020-1']=0
a4.ix['2020-2']=0
a4.ix['2020-3']=0
a4.ix['2020-4']=0
a4.ix['2020-5']=0
a4.ix['2020-6']=0
a4.ix['2020-7']=0

a5.ix['2019-9']=0
a5.ix['2019-10']=0
a5.ix['2019-11']=0
a5.ix['2019-12']=0
a5.ix['2020-1']=0
a5.ix['2020-2']=0
a5.ix['2020-3']=0
a5.ix['2020-4']=0
a5.ix['2020-5']=0
a5.ix['2020-6']=0
a5.ix['2020-7']=0

a6.ix['2019-10']=0
a6.ix['2019-11']=0
a6.ix['2019-12']=0
a6.ix['2020-1']=0
a6.ix['2020-2']=0
a6.ix['2020-3']=0
a6.ix['2020-4']=0
a6.ix['2020-5']=0
a6.ix['2020-6']=0
a6.ix['2020-7']=0

a7.ix['2019-11']=0
a7.ix['2019-12']=0
a7.ix['2020-1']=0
a7.ix['2020-2']=0
a7.ix['2020-3']=0
a7.ix['2020-4']=0
a7.ix['2020-5']=0
a7.ix['2020-6']=0
a7.ix['2020-7']=0

a8.ix['2019-12']=0
a8.ix['2020-1']=0
a8.ix['2020-2']=0
a8.ix['2020-3']=0
a8.ix['2020-4']=0
a8.ix['2020-5']=0
a8.ix['2020-6']=0
a8.ix['2020-7']=0

a9.ix['2020-1']=0
a9.ix['2020-2']=0
a9.ix['2020-3']=0
a9.ix['2020-4']=0
a9.ix['2020-5']=0
a9.ix['2020-6']=0
a9.ix['2020-7']=0

a10.ix['2020-2']=0
a10.ix['2020-3']=0
a10.ix['2020-4']=0
a10.ix['2020-5']=0
a10.ix['2020-6']=0
a10.ix['2020-7']=0

a11.ix['2020-3']=0
a11.ix['2020-4']=0
a11.ix['2020-5']=0
a11.ix['2020-6']=0
a11.ix['2020-7']=0

a12.ix['2020-4']=0
a12.ix['2020-5']=0
a12.ix['2020-6']=0
a12.ix['2020-7']=0

a13.ix['2020-5']=0
a13.ix['2020-6']=0
a13.ix['2020-7']=0

a14.ix['2020-6']=0
a14.ix['2020-7']=0

a15.ix['2020-7']=0

a=a1+a2+a3+a4+a5+a6+a7+a8+a9+a10+a11+a12+a13+a14+a15+a16

a['time']=[parser.parse(i) for i in a.index]
a=a.sort_values('time')
a=a.drop('time',axis=1)
j=0
for i in a.index:
    month=months('2019-4-30',i)
    if month>=1:
        a.iloc[j,0:month-1]=np.nan
        a.iloc[j,month+(mo-1):45]='-'
    a.iloc[j,month+(mo-1):45]='-'    
    j+=1
    
   
j=0
for i in a.index:    
    w=months("2020-2",i)
    if w>0:
        a.iloc[j,w-1]="-"
        j+=1

a.to_excel('Vintage90+.xlsx')



'------------滚动率------------------'
data56=pd.merge(data7_2,data8_2,on='库天下用户Id',how='inner') 
data56['逾期天数_x']=data56['逾期天数_x'].fillna(0)
data56['逾期天数_y']=data56['逾期天数_y'].fillna(0)
data56['滚动']=data56['逾期天数_x'].apply(lambda x:str(int(x)))+"--"+data56['逾期天数_y'].apply(lambda x:str(int(x)))

def label(x):
    x=int(x)
    la=pd.cut([x],[-9999,1,30,60,90,9999],labels=['M0','M1','M2','M3','M3+'],right=False)[0]
    return la

data=data1.copy()
data["label"]=data["逾期天数"].apply(lambda x:label(int(x)))
res=data.groupby("label")["账户已用额度"].sum()


data56['滚动label']=data56['滚动'].apply(lambda x:label(x.split('--')[0])+'--'+label(x.split('--')[1]))
data56['state']=data56['逾期天数_x'].apply(lambda x:label(int(x)))
data56['state1']=data56['逾期天数_y'].apply(lambda x:label(int(x)))

a=data56.groupby(['滚动label'])['账户已用额度_x'].count()
b=data56.groupby(['state'])['账户已用额度_x'].count()

result=df(np.zeros((5,5)));result.columns=['M0','M1','M2','M3','M3+']
result.index=['M0','M1','M2','M3','M3+']

for i in a.index:
    print(i)
    index=i.split('--')[0]
    columns=i.split('--')[1]
    result.loc[index,columns]=result.loc[index,columns]+a[i]  
    
 ### 看一下是怎么有N-M1的是否是需要账单对齐
data56.groupby('state').count()['账户已用额度_x']      
    
    
a=data56.pivot_table('逾期本金_x',columns=['滚动label'],index='年月_x',aggfunc='sum')
a=a[['M0--M0','M0--M1','M1--M2','M2--M3','M3--M4','M4--M5','M5--M6','M6--M6+']]
b=data56.pivot_table('逾期本金_x',columns=['state'],index='年月',aggfunc='sum')
b=b[['M0--M0','M0--M1','M1--M2','M2--M3','M3--M4','M4--M5','M5--M6','M6--M6+']]



#dd=pd.read_clipboard()
#d={}
#for i in dd.index:
#    for j in dd.columns:
#        d[i+'--'+j]=dd.loc[i,j]
#       
#s=df({0:d}).T


data1["逾期天数_1"]=data1["逾期天数"]
data2["逾期天数_2"]=data2["逾期天数"]
data3["逾期天数_3"]=data3["逾期天数"]
data4_2["逾期天数_4"]=data4_2["逾期天数"]
data5_2["逾期天数_5"]=data5_2["逾期天数"]
data6_2["逾期天数_6"]=data6_2["逾期天数"]
data7_2["逾期天数_7"]=data7_2["逾期天数"]
data_=pd.merge(data1,data2,on='寺库id')
data_=pd.merge(data_,data3,on='寺库id')
data_=pd.merge(data_,data4_2,on='寺库id')
data_=pd.merge(data_,data5_2,on='寺库id')
data_=pd.merge(data_,data6_2,on='寺库id')
data_=pd.merge(data_,data7_2,on='寺库id')


score=pd.read_excel(r'C:\Users\secoo\Desktop\模型日志文件\score.xlsx')
dd=pd.merge(score,data_,on='寺库id')[["年月_y","寺库id","逾期天数_1","逾期天数_2","逾期天数_3",
           "逾期天数_4","逾期天数_5","逾期天数_6","逾期天数_7","score"]]
dd.to_excel(r'C:\Users\secoo\Desktop\模型日志文件\score_overdue_8.xlsx',index=False)


#res=pd.pivot_table(data,values="账户已用额度",index="年月",columns="label",aggfunc="sum")
#
#data1=data[data["账户已用额度"]>0]
#res1=pd.pivot_table(data1,values="账户已用额度",index="年月",columns="label",aggfunc="count")
#
#res=data.groupby("年月")["账户信用额度"].sum()
#res1=data1.groupby("年月")["账户已用额度"].count()



##万霜报表

##资产规模结构
def label1(x):
    x=int(x)
    la=pd.cut([x],[-9999,1,31,61,91,121,151,181,9999],labels=['M0','M1','M2','M3','M4','M5','M6','M7+'],right=False)[0]
    return la

res=df()
for data in [data6,data7,data8,data9,data10,data11,data12,data1]:
    data["label"]=data["逾期天数"].apply(lambda x:label1(int(x)))
    re=df(data.groupby("label")["账户已用额度"].sum())
    res=pd.concat([re,res],axis=1)
    
    
##业务申请  
re1=data3.groupby("年月")["账户信用额度"].count()  ##授信通过件数
re2=data3.groupby("年月")["账户信用额度"].sum()  ##授信通过金额
