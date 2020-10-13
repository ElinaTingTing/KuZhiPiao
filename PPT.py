# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 09:24:04 2019

@author: secoo
"""


import pickle
import numpy as np
import pandas as pd


f_=open('data11.pkl','rb')
data11=pickle.load(f_)
f_.close()

data_web=pd.read_excel(r'data_web.xlsx')
merge=pd.merge(data_web,data11,left_on="unique_id",right_on="寺库id",how="left")


merge["zi_pass1"]=np.where(merge["acc_lmt"].isnull(),0,1)


merge["zi_pass"]=np.where(merge["refuse_desc"].isnull(),0,1)  ##0是通过，1是拒绝，自授信的通过拒绝
merge["real_pass"]=np.where(merge["寺库id"].isnull(),1,0)  ##0通过，11是拒绝，真实的通过和拒绝

renshu=pd.pivot_table(merge,values="ID_NO",index="zi_pass",columns=["CUSTOMER_CHANNEL","real_pass"],aggfunc="count")
merge_30=merge[merge["逾期天数"]>=30]
zi=pd.pivot_table(merge_30,values="逾期本金",index="zi_pass",columns=["CUSTOMER_CHANNEL","real_pass"],aggfunc="sum")


mu=pd.pivot_table(merge,values="累计订单金额",index="zi_pass",columns=["CUSTOMER_CHANNEL","real_pass"],aggfunc="sum")


data11['授信时间']=pd.to_datetime(data11['授信时间'].apply(lambda x:x.split(' ')[0]))
data1111=data11[(data11['授信时间']>'2018-12-31')&(data11["授信时间"]<'2019-11-01')]
data1111['年月']=data1111['授信时间'].apply(lambda x:str(x.year)+'-'+str(x.month))
data1111.to_excel("sss.xlsx")



renshu=pd.pivot_table(merge,values="ID_NO",index="zi_pass",columns=["CUSTOMER_CHANNEL","渠道"],aggfunc="count")

merge_30=merge[merge["逾期天数"]>=30]
zi=pd.pivot_table(merge_30,values="逾期本金",index="zi_pass",columns=["CUSTOMER_CHANNEL","渠道"],aggfunc="sum")
mu=pd.pivot_table(merge,values="累计订单金额",index="zi_pass",columns=["CUSTOMER_CHANNEL","渠道"],aggfunc="sum")

zi=pd.pivot_table(merge,values="逾期本金",index="zi_pass",columns=["CUSTOMER_CHANNEL","渠道"],aggfunc="sum")


























ss="预付费/教育/健身/医美/信用卡分期"
s1=ss.split("/")
aa="管理办法/发布/发文/监管/新规/人民银行/银监会/部委/号文/教育部"
a1=aa.split("/")


re=[]
for i in s1:
    for j in a1:
        re.extend([i+j])