# Program to multiply two matrices using nested loops
import random
import numpy as np
# from memory_profiler import profile

N = 250
# NxN matrix
X = np.random.randint(0,100, size = (N, N))
# NxN matrix
# X = []
# for i in range(N):
#     X.append([random.randint(0,100) for r in range(N)])

# Nx(N+1) matrix
Y  = np.random.randint(0,100, size = (N, N+1))
# Y = []
# for i in range(N):
#     Y.append([random.randint(0,100) for r in range(N+1)])

# result is Nx(N+1)
result = np.dot(X,Y)
# result = []
# for i in range(N):
#     result.append([0] * (N+1))

# # iterate through rows of X
# for i in range(len(X)):
#     # iterate through columns of Y
#     for j in range(len(Y[0])):
#         # iterate through rows of Y
#         for k in range(len(Y)):
            # result[i][j] += X[i][k] * Y[k][j]
"""
delete print to improve speed (3a)
"""
# for r in result:
#     print(r)

print(result)