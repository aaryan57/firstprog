#EXPERIMENT 10 Page Rank
n = 4
adj_mat =  [[0, 1, 1, 1],
            [0, 0, 0, 1],
            [1, 0, 0, 1],
            [1, 0, 1, 0]]
print("Entered Adjacency Matrix is:")
for row in adj_mat:
    print(row)
# Calculate out-degree of each node
out_degree = []
for i in range(n):
    out_count = 0
    for j in range(n):
        if adj_mat[i][j] == 1:
            out_count += 1
    out_degree.append(out_count)
print("\nTotal Outgoing Links from Each Node:")
for i in range(n):
    print(f"Node {i+1}: {out_degree[i]}")
print(out_degree)
# Calculate Transition Probability Matrix
A = []
for i in range(n):
    A_row = []
    for j in range(n):
        if adj_mat[j][i] == 1:
            A_row.append(1/out_degree[j])
        else:
            A_row.append(0)
    A.append(A_row)
print("\nTransition Probability Matrix A:")
for row in A:
    print(row)
print()
import numpy as np
X = np.ones((n, 1))
A = np.array(A)
prev = np.array([])
print("\nFinal matrix after 3 iterations\n")
for _ in range(0, 3):
    X = A @ X
    prev = X
print(X)
# Sorting the values of the pages in descending order using dictionary
ans = dict()
for _ in range(0, X.size):
    ans[f'Page {_+1}'] = X[_][0]
ans = dict(sorted(ans.items(), key=lambda item: -item[1]))
print()
print(ans)
print()
ctn = 1
for i in ans:
    print(f"Rank {ctn}: {i}")
ctn+=1