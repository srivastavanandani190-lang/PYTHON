import numpy as np
print(np.__version__)

arr_1d=np.array([1,2,3,4])
print("One D array:",arr_1d)
print(type(arr_1d))

arrt_1d=np.array((1,2,3,4))
print("One D array:",arrt_1d)
print(type(arrt_1d))

arr_2d=np.array([[1,2,3],[4,5,6],[12,13,45],[4,8,9]])
print("Two D array:",arr_2d)
print(arr_2d[0,2])#[0][2]

#numpy.random.rand()->0to1(float)
x=np.random.rand(3,4)
print(x)
y=np.random.randint(3,12,size=4)
print(y)
z=np.random.choice([1,2,3,4,5,6])
print(z)
z1=np.random.choice([1,2,3,4,5,6],size=(2,3))
print(z1)

#boolean array indexing
x1=np.array([10,23,45,67,89])
x1[x1%5]==0
print(x1)
 
#reshaping 
n=np.arange(1,13)
print(n)
print(n.reshape((3,4)))
print(n.reshape((4,3)))
print(n.reshape((2,6)))
print(n.reshape((6,2)))
#copy vs view
#copy->different loction different reference
#view ->different conatiner same reference
#x.T x=0row x=1column
array=np.array([[1,2],[3,4],[8,9],[5,6]])
print(np.rot90(array,2))

