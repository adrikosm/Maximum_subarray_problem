import numpy as np
import time

start_time = time.time()
np.random.seed(1069274)


def CeilIndex(A, l, r, key):
    while (r - l > 1):
        m = l + (r - l) // 2
        if (A[m] >= key):
            r = m
        else:
            l = m
    return r


def LongestIncreasingSubsequenceLength(A, size):
    tailTable = [0 for i in range(size + 1)]
    tailTable[0] = A[0]
    len = 0
    sumx = 0
    for i in range(0, size):
        if (A[i] < tailTable[0]):
            print(A[i])
            tailTable[i] = A[i]
            sumx += A[i]
        elif (A[i] > tailTable[len - 1]):
            tailTable[len] = A[i]
            print(A[i])
            sumx += A[i]
            len += 1
        else:
            tailTable[CeilIndex(tailTable, i, len - 1, A[i])] = A[i]
    return sumx


np.random.seed(1069274)

# random_numbers = np.random.randint(-100, 100, size=100)
random_numbers = [4, -1, 2, 1]
n = len(random_numbers)
print("Max Contiguous Number found ", LongestIncreasingSubsequenceLength(random_numbers, n))
print("--- %s seconds ---" % (time.time() - start_time))
