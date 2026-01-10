import numpy as np
from sympy import primerange
from numpy.linalg import eigvals

def goldbach_matrix(N):
    primes = list(primerange(2, N))
    index = {p:i for i,p in enumerate(primes)}
    M = len(primes)
    A = np.zeros((M, M))
    
    for i, p in enumerate(primes):
        q = N - p
        if q in index:
            j = index[q]
            A[i, j] = 1
    return A

def critical_coupling(N):
    A = goldbach_matrix(N)
    lambda_max = max(np.real(eigvals(A)))
    if lambda_max == 0:
        return np.inf
    return 1 / lambda_max
