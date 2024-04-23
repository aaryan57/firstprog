n = 4
adj = [
    [0, 1, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
    [1, 0, 1, 0]
]
for row in adj:
    print(row)

out_look = []
for i in range(n):
    outCount = 0
    for j in range(n):
        if( adj[i][j] ==1 ):
            outCount+= 1
    out_look.append(outCount)
print()
print(out_look)
print()
A = []
print("transititional matrix is")
for i in range(n):
    A_row=[]
    for j in range(n):
        if( adj[j][i] == 1):
            A_row.append(1/out_look[j])
        else:
            A_row.append(0)
    A.append(A_row)
for row in A:
    print(row)

import numpy as np

X=np.ones((n , 1))
A=np.array(A)
prev=np.array([])
print("final matrix is")
for _ in range(0,3):
    X=A @ X
    prev=X
for row in X:
    print(row)
















