import pandas as pd
import numpy as np

a = pd.Series([1,2,3])
print(a)


#index functionality of series
ab=pd.Series([1,2,3],index=["a",'b','c'])
print(ab)

#passing list directly into panda series
l=[1,'anc',2,3]
aa = pd.Series(l)
print(aa)

#passing dictionry into panda series (works according to value) 
d={1:'a',2:'b'}
ac = pd.Series(d)
print(ac)

d1={'a':1.0,'b':2.0}
ax = pd.Series(d1)
print(ax)

#passing numpy array to panda series


#list of string into p series
az = pd.Series(['i','am'])
print(az)

#Range in Pandas
aq = pd.Series(15,index=range(1,10,2))
print(aq)

#
city=['indore','bhopal']
ps=pd.Series(15,index=city)
print(ps)

#both city and pincode are dynamic
pinc=[450001,452020]
cc = pd.Series(pinc,index=city)
print(cc)

#abhi
days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
time=['2 hrs','6 hrs','7hrs','2 hrs','6 hrs','7hrs','3 hrs']
abhi= pd.Series(time,index=days)
print(abhi)

#challange
n=int(input('r'))
nn=int(input('rr'))
av = pd.Series(range(n+3,nn+3,7),index=range(n,nn,7))
print(av)

















