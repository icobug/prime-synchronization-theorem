import math
import numpy as np
from time import time

def sieve(n):
    is_prime = np.ones(n+1, dtype=bool)
    is_prime[:2] = False
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            is_prime[i*i:n+1:i] = False
    return np.where(is_prime)[0]

def gamma_goldbach(N, primes_set):
    s = 0.0
    for p in primes_set:
        if p > N//2: break
        q = N - p
        if q in primes_set:
            s += 1.0 / (math.log(p) * math.log(q))
    return s

Nmax = 100000
start = time()
primes = sieve(Nmax)
primes_set = set(primes)

# Example calculation
g = gamma_goldbach(Nmax, primes_set)
print(f"Nmax = {Nmax}")
print(f"Gamma(N) = {g}")
print(f"Elapsed time = {time()-start:.2f} seconds")