"""
numpy stands for Numerical Python is a python library that is commonly used for numerical computation.
It provides a powerful N-dimensional array object, as well as tools for working with these arrays.
creator: Travis Oliphant in 2005
pip install numpy
array()
ndim
size
nbytes
itemsize
dtype
slicing[:] in 1d araay
2d array [r,c]/[r],[r,:]
np.ones((v1,v2,v3))
np.zeros((v1,v2,v3))
np.float((r,c),value)

"""
import numpy as np
from numpy import random
#creating an array
#1d array
arr1=np.array([1,2,3,4,5])
print(arr1.ndim," dimensional",arr1)
#0d array
arr2=np.array(10)
print(arr2.ndim," dimensional",arr2)
#2d array
arr3=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr3.ndim," = ",arr3)
#number of element
print(arr3.size)
#total memory taken by an array
print(arr3.nbytes)
#memory taken by an array element
print(arr3.itemsize)
#data type of an array
print(arr2.dtype)
#specific element in an array
print(arr3[0,2])
#specific row in an array
print(arr3[2,:])#single value
#specific bunch of elements/slicing in an array
print(arr1[2:3])
print(arr3[2,:])
#copy of an array
carr=arr3.copy()
print(carr)
#zero matrix
mtx=np.zeros((4,6))
print(mtx)
print(mtx.dtype)
#all one matrix
#in 3 parameters first will shows the number of matrix,no.of row,no. of columns
mtx1=np.ones((2,4,5))
#specific element matrix
mtx3=np.full((3,4),10)
print(mtx3)
#decimal no. array
rarr=np.random.rand(3,5)
print(rarr)
#identity matrix
a=np.identity(4)
print(a)
#performing plus operation
print(arr1+3)
#performing minus operation
print(arr1-3)
print(arr1*4)
print(np.array([1,2,3,4])+np.array([2,3,4,8]))
#cos in an array
print(np.cos(arr1))
#sin
print(np.sin(arr1))
#finding minimum and maximum value in an array
print(np.min(arr3))
print(np.max(arr3))
#sum
print(np.sum(arr3))
#iteration in 1d array
for i in arr1:
    print(i)
#iteration in 2d array
for i in arr3:
    for j in i:
        print(j)