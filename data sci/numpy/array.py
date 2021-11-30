import numpy as np


#np.array([]) creates an array 
n = np.array([1,2,3])
print(n)

#design 2d array of 3x3 matrix
n1=np.array([[1,2,3],[9,4,3],[0,0,0]])
print(n1)

#type function
print(type(n))
print(type(n1))

#making azero matrix
#for single dimension
n=np.zeros(3)
print(n)
#for 2 dimension
n1=np.zeros((3,3))
print(n1)

#making a matrix like this
'''[[70 70 70 70 70]
 [70 70 70 70 70]
 [70 70 70 70 70]
 [70 70 70 70 70]
 [70 70 70 70 70]]
'''
n2=np.full((5,5),70)
print(n2)

#works similar as for i in range (7,70,5)
n3=np.arange(7,70,5)
print(n3)

#print table of 972 in reverse order
n4 = np.arange(9720,971,-972)
print(n4)

#RANDOM
n5 = np.random.randint(1,10)
print(n5)

n5 = np.random.randint(1,10,2)
print(n5)

#transpose of a matrix
n6 = np.array([[1,2,3],[1,1,1],[1,1,1],[5,5,5]])
n6.shape=(3,4)
print(n6)










