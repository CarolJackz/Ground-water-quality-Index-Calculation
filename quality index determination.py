#!/usr/bin/env python
# coding: utf-8

# In[113]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
from matplotlib import pyplot as plt
df=pd.read_excel("C:/Users/Lenovo/Desktop/works/quality/waterquality.xlsx")
from scipy import stats
from scipy.stats import pearsonr


# In[114]:


df.shape


# In[115]:


df.describe()


# In[116]:


df.info()


# In[117]:


df1 = df.iloc[:,3:22 ]
df1.head(5)


# In[118]:


# Correlation between different variables
cor_mat=df1.corr().round(2)
cor_mat
#Set up the matplotlib plot configuration
plt.figure(figsize=(14,14))
# Draw the heatmap
plot=sns.heatmap(cor_mat,annot=True)


# In[119]:


import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
# the independent variables set
X = df[list(df.columns[6:22])]
# VIF dataframe
vif_data=pd.DataFrame()
vif_data["feature"]=X.columns
# calculating VIF for each feature
vif_data["VIF"] = [variance_inflation_factor(X.values, i)
                          for i in range(len(X.columns))]
print(vif_data)


# In[120]:


def cal(c,w,s):
    r_w=w/45
    wqi=r_w*(c/s)*100
    return wqi
x=cal(df1.Ca,3,75)
df1["ca_index"]=x
df1


# In[121]:


def cal(c,w,s):
    r_w=w/45
    wqi=r_w*(c/s)*100
    return wqi
x=cal(df1.TH,2,300)
df1["TH_index"]=x
df1


# In[122]:


def cal(c,w,s):
    r_w=w/45
    wqi=r_w*(c/s)*100
    return wqi
x=cal(df1.Mg,3,30)
df1["Mg_index"]=x
df1


# In[123]:


def cal(c,w,s):
    r_w=w/45
    wqi=r_w*(c/s)*100
    return wqi
x=cal(df1.Cl,3,200)
df1["Cl_index"]=x
df1


# In[124]:


def cal(c,w,s):
    r_w=w/45
    wqi=r_w*(c/s)*100
    return wqi
x=cal(df1.SO4,5,200)
df1["SO4_index"]=x
df1


# In[125]:


def cal(c,w,s):
    r_w=w/45
    wqi=r_w*(c/s)*100
    return wqi
x=cal(df1.F,5,1.5)
df1["F_index"]=x
df1


# In[126]:


def cal(c,w,s):
    r_w=w/45
    wqi=r_w*(c/s)*100
    return wqi
x=cal(df1.NO3,5,45)
df1["NO3_index"]=x
df1


# In[127]:


def cal(c,w,s):
    r_w=w/45
    wqi=r_w*(c/s)*100
    return wqi
x=cal(df1.TDS,2,500)
df1["TDS_index"]=x
df1


# In[128]:


def cal(c,w,s):
    r_w=w/45
    wqi=r_w*(c/s)*100
    return wqi
x=cal(df1.HCO3,4,300)
df1["HCO3_index"]=x
df1


# In[129]:


def cal(c,w,s):
    r_w=w/45
    wqi=r_w*(c/s)*100
    return wqi
x=cal(df1.K,3,10)
df1["K_index"]=x
df1


# In[130]:


def cal(c,w,s):
    r_w=w/45
    wqi=r_w*(c/s)*100
    return wqi
x=cal(df1.Na,3,200)
df1["Na_index"]=x
df1


# In[131]:


def cal(c,w,s):
    r_w=w/45
    wqi=r_w*(c/s)*100
    return wqi
x=cal(df1.EC,3,1500)
df1["EC_index"]=x
df1


# In[132]:


def cal(c,w,s):
    r_w=w/45
    wqi=r_w*(c/s)*100
    return wqi
x=cal(df1.PH,4,1500)
df1["PH_index"]=x
df1


# In[133]:


c=df1.iloc[:,18:]
final_index=c.sum(axis=1)
df1['final_index']=final_index
df1


# In[ ]:





# In[134]:


#Classification of water quality index based on calculated WQI values[Ramakrishnaiah et al.2009]


# In[136]:


WQ_class=[]
for row in df1['final_index']:
    if row <50: WQ_class.append('Excellent')
    elif row <100: WQ_class.append('Good')
    elif row <150: WQ_class.append('Poor')
    elif row <200: WQ_class.append('Very Poor')
    elif row >200: WQ_class.append('Unsuitable')
df1['WQ_class']=WQ_class
df1


# In[138]:


df1.to_excel("C:/Users/Lenovo/Desktop/works/quality/waterquality_index_final.xlsx",index=False)


# In[ ]:




