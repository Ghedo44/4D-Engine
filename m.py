import numpy as np 

A=np.array([[2,6,1],[2,0,4],[1,2,-1]])
b=np.array([2,0,1])
r=np.linalg.matrix_rank(A)
k=np.linalg.solve(A, b)

print(k , r)

# Ax = b --> x = A^-1 b
print(np.dot(np.linalg.inv(A),b))