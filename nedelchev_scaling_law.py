import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eigvals
from scipy.stats import linregress

def primes_upto(n):
    primes = []
    for p in range(2, n):
        for i in range(2, int(p**0.5) + 1):
            if p % i == 0:
                break
        else:
            primes.append(p)
    return np.array(primes, dtype=float)

def goldbach_matrix(primes, N):
    m = len(primes)
    W = np.zeros((m, m))
    idx = {p:i for i,p in enumerate(primes)}
    for i,p in enumerate(primes):
        q = N - p
        if q in idx:
            W[i, idx[q]] = 1.0
    return W

def critical_kappa(N):
    primes = primes_upto(N)
    if len(primes) < 5: return np.nan
    omega = primes
    sigma = np.std(omega)
    W = goldbach_matrix(primes, N)
    if np.count_nonzero(W) == 0: return np.nan
    lambda_max = max(abs(eigvals(W)))
    return sigma / lambda_max

# Scale Test
N_vals = np.array([100, 150, 200, 300, 400, 600, 800, 1000])
kc_vals = np.array([critical_kappa(N) for N in N_vals])

mask = np.isfinite(kc_vals)
slope, intercept, r, _, _ = linregress(np.log(N_vals[mask]), np.log(kc_vals[mask]))

print(f"Scaling Result: Alpha = {slope:.4f}, R2 = {r**2:.5f}")

plt.figure(figsize=(8,5))
plt.loglog(N_vals, kc_vals, 'o-', label='Measured κc(N)')
plt.loglog(N_vals, np.exp(intercept)*N_vals**slope, '--', label=f'Fit: κc ~ N^{slope:.2f}')
plt.xlabel("N")
plt.ylabel("κc")
plt.title("Goldbach–Kuramoto Scaling Law")
plt.grid(True, which="both")
plt.legend()
plt.show()