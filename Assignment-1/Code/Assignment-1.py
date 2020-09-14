import numpy as np

A = np.array([3,1])
M = np.array([1,-1])
B = np.array([-1,2])

lambda1=-4
#First Intersection Point: X1=A+lambda1*M
X1 = np.add(A,lambda1*M)

# Direction Vector_1: V1=B-X1
V1 = np.subtract(B,X1)

lambda2=-1
#Second Intersection Point: X2=A+lambda2*M
X2 = np.add(A,lambda2*M)

# Direction Vector_2: V2=B-X2
V2 = np.subtract(B,X2)

print("Intersection Points:")
print(X1, X2)
print("Direction Vectors:")
print(V1, V2)
