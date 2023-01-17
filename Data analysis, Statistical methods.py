#!/usr/bin/env python
# coding: utf-8

# # <font color = black> </font> Data Analysis

# In[1]:


1. #Finding central tendencies of data
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[2]:


df = pd.read_csv('C:\\Users\\MALLIKA\\Downloads\\Assignmentdatafoodsales.csv')


# In[3]:


df.head()


# In[11]:


#Finding central Tendencies
a= df['TotalPrice'].describe()


# In[12]:


a


# In[15]:


a['var']= a['std']**2
a.round(2)


# In[111]:


import statistics as t 
v1=t.median(df['TotalPrice'])
v2=t.mode(df['TotalPrice'])
print(v1, v2)


# In[16]:


a.to_csv("Assignment.csv")


# # <Font color= Black> </Font>2. Finding the Skewness and kurtosis
# 

# In[45]:


#Shows normal distribution 
import seaborn as sns 
plt.figure(figsize=(16,6)) 
plt.subplot(121) 
normalr=np.random.normal(136.58,108.35,(1000,1)) 
sns.distplot(normalr) 
#Shows right skew in total price 
plt.subplot(122) 
sns.distplot(df.TotalPrice)


# In[29]:


df.skew() #skewness is considerably high if greater than 0.75


# In[41]:


plt.subplot(122)
sns.distplot(df.UnitPrice) 

plt.subplot(121)
sns.distplot(df.Quantity) 
#The results show right skewness


# In[42]:


df.kurtosis()


# In[ ]:


#Quantity is Fat Tailed- PlatyKurtic
#UnitPrice is This Tailed- LeptoKurtic
#TotalPrice is Fat Tailed- PlatyKurtic


# # <Font color=Black> </Font> 3. Find the mean difference between region for quantity and total prices

# In[47]:


import scipy.stats as stats


# In[48]:


x= df[['Quantity']]
y= df[['TotalPrice']]


# In[59]:


#T TEST Quantity
stats.ttest_ind(df['Quantity'][df['Region'] == 'East'],
df['Quantity'][df['Region'] == 'West'])


# In[60]:


# T Test Total Price
stats.ttest_ind(df['TotalPrice'][df['Region'] == 'East'],
df['TotalPrice'][df['Region'] == 'West'])


# In[61]:


#T TEST QUANTITY & TOTAL PRICE - REGION- EAST
stats.ttest_ind(df['Quantity'][df['Region'] == 'East'],
df['TotalPrice'][df['Region'] == 'East'])


# In[62]:


#T TEST QUANTITY & TOTAL PRICE - REGION- West
stats.ttest_ind(df['Quantity'][df['Region'] == 'West'],
df['TotalPrice'][df['Region'] == 'West'])


# In[64]:


#One way Anova region East
A = df['Quantity'][df['Region'] == 'East']
B = df['TotalPrice'][df['Region'] == 'East']


# In[68]:


fvalue, pvalue = stats.f_oneway(A,B)
print(fvalue, pvalue)


# In[69]:


#One way Anova region West
A = df['Quantity'][df['Region'] == 'West']
B = df['TotalPrice'][df['Region'] == 'West']


# In[70]:


fvalue, pvalue = stats.f_oneway(A,B)
print(fvalue, pvalue)


# # <font color = 'Black'></Font> 4. Find the sample variance among the Category for quantity and total prices

# In[92]:


import statsmodels.api as sm


# In[93]:


from statsmodels.formula.api import ols


# In[105]:


anovaquan = sm.stats.anova_lm(model, typ=2)
anovaquan


# In[ ]:


# P value > 0.05 means no subsequent effect of categories and Quantity on total price


# In[79]:


#Sample Variance For Quantity - Categories 1. Bars 2.Crackers 3. Cookies 4. Snacks

var1 = df['Quantity'][df['Category']== 'Bars']
var2 = df['Quantity'][df['Category']== 'Crackers']
var3 = df['Quantity'][df['Category']== 'Cookies']
var4 = df['Quantity'][df['Category']== 'Snacks']


# In[85]:


a=stats.tvar(var1)
b=stats.tvar(var2)
c=stats.tvar(var3)
d =stats.tvar(var4)
print(a,b,c,d)


# In[86]:


#Sample Variance For TotalPrices - Categories 1. Bars 2.Crackers 3. Cookies 4. Snacks
var1 = df['TotalPrice'][df['Category']== 'Bars']
var2 = df['TotalPrice'][df['Category']== 'Crackers']
var3 = df['TotalPrice'][df['Category']== 'Cookies']
var4 = df['TotalPrice'][df['Category']== 'Snacks']


# In[87]:


a=stats.tvar(var1)
b=stats.tvar(var2)
c=stats.tvar(var3)
d =stats.tvar(var4)
print(a,b,c,d)


# # <font color= 'Black'> </font> 5. Find the sample variance among the Product for quantity and total prices

# In[109]:


model = ols('TotalPrice ~ Product+Quantity', data=df).fit()
anovaprod = sm.stats.anova_lm(model, typ=2)
anovaprod


# In[ ]:


# P value > 0.05 means no subsequent effect of categories and Quantity on total price


# In[88]:


#Sample Variance For Quantity - Product 1. Carrot 2.Whole Wheat 3. Chocochip 4.ArrowRoot 5.OatmealRaisin 6.Bran 7. Potato Chips 8. Pretzel

var1 = df['Quantity'][df['Product']== 'Carrot']
var2 = df['Quantity'][df['Product']== 'Whole Wheat']
var3 = df['Quantity'][df['Product']== 'Choco Chip']
var4 = df['Quantity'][df['Product']== 'Arrowroot']
var5 = df['Quantity'][df['Product']== 'Bran']
var6 = df['Quantity'][df['Product']== 'Oatmeal Raisin']
var7 = df['Quantity'][df['Product']== 'Potato Chips']
var8 = df['Quantity'][df['Product']== 'Pretzel']


# In[89]:


a=stats.tvar(var1)
b=stats.tvar(var2)
c=stats.tvar(var3)
d =stats.tvar(var4)
e =stats.tvar(var5)
f =stats.tvar(var6)
g =stats.tvar(var7)
h= stats.tvar(var8)

print(a,b,c,d,e,f,g,h)


# In[90]:


#Sample Variance For Total Price - Product 1. Carrot 2.Whole Wheat 3. Chocochip 4.ArrowRoot 5.OatmealRaisin 6.Bran 7. Potato Chips 8. Pretzel

var1 = df['TotalPrice'][df['Product']== 'Carrot']
var2 = df['TotalPrice'][df['Product']== 'Whole Wheat']
var3 = df['TotalPrice'][df['Product']== 'Choco Chip']
var4 = df['TotalPrice'][df['Product']== 'Arrowroot']
var5 = df['TotalPrice'][df['Product']== 'Bran']
var6 = df['TotalPrice'][df['Product']== 'Oatmeal Raisin']
var7 = df['TotalPrice'][df['Product']== 'Potato Chips']
var8 = df['TotalPrice'][df['Product']== 'Pretzel']


# In[91]:


a=stats.tvar(var1)
b=stats.tvar(var2)
c=stats.tvar(var3)
d =stats.tvar(var4)
e =stats.tvar(var5)
f =stats.tvar(var6)
g =stats.tvar(var7)
h= stats.tvar(var8)

print(a,b,c,d,e,f,g,h)


# In[ ]:




