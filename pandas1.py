from pandas import * #wes mckinney 2008
from numpy import * #travis oliphant 2005
ser=Series(random.rand(10))
#print(ser)
print(type(ser))
print(ser.index)
print(ser.dtype)
print(ser.head(7))
df=DataFrame(random.rand(5,4),index=arange(5))
#print(df)
#print(df.columns)
arr=df.to_numpy()
#print(type(arr))
csv=df.to_csv('new.csv',index=False)
new_csv=read_csv('new.csv')
print(new_csv)

df.columns=list('abcd')
print(df.loc[0,'a'])
print(df.index)
df.drop([0,1],axis=0,inplace=True)
print(df)

#checking for null value in Df
#df['a'][2]=56.9
print(df)
#covert dictionary to dataframe
dict={
    "name":["aryan","pankaj","pooja",None],
    "age":[22,23,27,30]
}
data=DataFrame(dict)
data.to_csv('data.csv',index=False)
a=data.dropna()
print(a)

