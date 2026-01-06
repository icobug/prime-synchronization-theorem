# ============================================================
# NEDELCHEV DYNAMICAL SCALING LAW (v4.0)
# Measurement of Critical Coupling (Kc) in Kuramoto Dynamics
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from sklearn.linear_model import LinearRegression

# 1. SETUP: Prime Generation
def get_primes(n):
    sieve = np.ones(n, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n:i] = False
    return np.where(sieve)[0].astype(float)

# 2. DYNAMICS: Kuramoto with Goldbach Coupling
def kuramoto_deriv(theta, t, omega, W, K, M):
    diff = theta[:, None] - theta
    interaction = np.sum(W * np.sin(diff), axis=1)
    return omega + (K / M) * interaction

def get_order_parameter(N, K, duration=20):
    primes = get_primes(N)
    M = len(primes)
    omega = primes  # Natural frequencies are the primes themselves
    
    # Goldbach Matrix
    p_set = set(primes)
    W = np.zeros((M, M))
    for i, p in enumerate(primes):
        target = N - p
        if target in p_set:
            j = np.where(primes == target)[0][0]
            W[i, j] = 1.0
            
    theta0 = np.random.uniform(0, 2*np.pi, M)
    t = np.linspace(0, duration, 100)
    sol = odeint(kuramoto_deriv, theta0, t, args=(omega, W, K, M))
    
    final_theta = sol[-1]
    R = np.abs(np.mean(np.exp(1j * final_theta)))
    return R

# 3. MEASUREMENT: Search for Kc (where R crosses 0.5)
def find_kc(N):
    low, high = 0, N * 2.5
    for _ in range(10):  # Binary search for precision
        mid = (low + high) / 2
        if get_order_parameter(N, mid) > 0.5:
            high = mid
        else:
            low = mid
    return (low + high) / 2

# --- EXECUTION ---
N_vals = [200, 300, 400, 500, 600, 700, 800]
kc_results = []

print("Running Dynamical Scaling Test (v4)...")
for N in N_vals:
    kc = find_kc(N)
    kc_results.append(kc)
    print(f"N={N:4d} | Measured Kc ≈ {kc:.2f}")

# --- ANALYSIS ---
X = np.array(N_vals).reshape(-1, 1)
y = np.array(kc_results)
model = LinearRegression().fit(X, y)
alpha = model.coef_[0]
r2 = model.score(X, y)

print(f"\nScaling Slope (alpha): {alpha:.4f}")
print(f"R-squared: {r2:.5f}")

# --- PLOT ---
plt.figure(figsize=(10, 6))
plt.scatter(N_vals, kc_results, color='green', s=100, label="Simulation Data")
plt.plot(N_vals, model.predict(X), 'k--', label=f"Scaling Law (Kc ≈ {alpha:.2f}*N)")
plt.title("Dynamical Scaling of Goldbach Resonance", fontsize=14)
plt.xlabel("N (Number Scale)", fontsize=12)
plt.ylabel("Critical Coupling (Kc)", fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()