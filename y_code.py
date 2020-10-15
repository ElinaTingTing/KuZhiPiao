# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 10:28:50 2020

@author: secoo
"""
import numpy as np  
import pandas as pd
import pickle as pkl
from pandas import DataFrame as df


## 授信额度划分
def amountformat (amount): 
    result=pd.cut([amount],[-9999,2000,4000,6000,8000,10000,15000,20000,30000,999999],\
                  labels=['0-2000','2000-4000','4000-6000',\
                  '6000-8000','8000-10000','10000-15000',\
                  '15000-20000','20000-30000','30000+'],right=True)   
    return result

## 逾期时间划分 
def duedays (days):
    if days<=0:
        return '0'
    elif days>0 and days<=30:
        return '0-30'
    elif days <=90:
        return '30-90'
    else:
        return '90+'



f_=open('data9_2.pkl','rb')
data=pkl.load(f_)
f_.close()
data1=data.copy()

data=data.drop_duplicates()
data=data[data['渠道']!='京东白条']
data['逾期天数'][data['逾期本金']==0]=0

data['date']=data['授信时间'].apply(lambda x: x[0:7] )
data['授信额度划分']=data['账户信用额度'].map(lambda x: amountformat(x)[0])
data['逾期']=data['逾期天数'].apply(lambda x: duedays(x))


##授信时间-额度划分
a1=data.groupby(['date','授信额度划分'])['账户编号'].count()
a2=data.groupby('date')['账户编号'].count()
res=(a1/a2).unstack().fillna(0)

a1=data.groupby('授信额度划分')['账户编号'].count()
a2=data.shape[0]
res=a1/a2



##授信渠道-额度划分
a1=data.groupby(["渠道","授信额度划分"])["账户编号"].count()
a2=data.groupby("渠道")["账户编号"].count()
res=(a1/a2).unstack().fillna(0)

##授信额度-逾期
a1=data.groupby(['授信额度划分','逾期'])['账户编号'].count()
a2=data.groupby('授信额度划分')['账户编号'].count()
res=(a1/a2).unstack().fillna(0)

a1=data.groupby('逾期')['账户编号'].count()
a2=data.shape[0]
res=a1/a2


##授信额度-逾期金额
a1=data.groupby(['授信额度划分','逾期'])['逾期本金'].sum().unstack()
a2=data.groupby(['授信额度划分','逾期'])['账户已用额度'].sum().unstack()##用于获取未逾期的金额


##授信额度-额度使用
a1=data.groupby('授信额度划分')['账户已用额度'].sum()
a2=data.groupby('授信额度划分')['账户信用额度'].sum()
