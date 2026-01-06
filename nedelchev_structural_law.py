# ============================================================
# THE NEDELCHEV STRUCTURAL LAW: SPECTRAL INVARIANCE
# Discovery: Universal Stability of Goldbach Arithmetic Networks
# ============================================================

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def get_primes(n):
    """Sieve of Eratosthenes to generate primes up to n."""
    sieve = np.ones(n, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n:i] = False
    return np.where(sieve)[0]

def goldbach_matrix(N):
    """Generates the Goldbach connectivity matrix for a given N."""
    primes = get_primes(N)
    M = len(primes)
    idx = {p: i for i, p in enumerate(primes)}
    
    W = np.zeros((M, M))
    for i, p in enumerate(primes):
        q = N - p
        if q in idx:
            W[i, idx[q]] = 1.0
    return W

def run_stability_test(Ns):
    """Measures the Spectral Radius and Critical Coupling for various scales."""
    kc_vals = []
    lambda_max_vals = []
    
    print(f"{'N':>5} | {'λ_max':>10} | {'κc (1/λ)':>10}")
    print("-" * 35)
    
    for N in Ns:
        W = goldbach_matrix(N)
        # Calculate eigenvalues
        eigs = np.linalg.eigvals(W)
        l_max = np.max(np.abs(eigs))
        
        # In the Nedelchev Law, Kc = 1 / lambda_max
        # Since lambda_max = 1 for Goldbach, Kc = 1
        kc = 1.0 / l_max if l_max > 0 else np.nan
        
        lambda_max_vals.append(l_max)
        kc_vals.append(kc)
        print(f"{N:5d} | {l_max:10.3f} | {kc:10.3f}")
        
    return np.array(kc_vals)

# --- EXECUTION ---
N_range = [200, 300, 400, 500, 600, 700, 800, 900, 1000]
print("Starting Nedelchev Structural Law Verification...")
kc_measured = run_stability_test(N_range)

# --- LINEAR REGRESSION (SCALING ANALYSIS) ---
X = np.array(N_range).reshape(-1, 1)
y = kc_measured

model = LinearRegression().fit(X, y)
alpha = model.coef_[0]
r_squared = model.score(X, y)

print("\n" + "="*30)
print("FINAL RESULTS:")
print(f"Scaling Slope (α): {alpha:.5f} (Target: 0.0000)")
print(f"Confidence (R²):   {r_squared:.5f} (Target: 1.0000)")
print("="*30)

# --- VISUALIZATION ---
plt.figure(figsize=(10, 6))
plt.scatter(N_range, kc_measured, color='blue', s=100, label="Measured Stability Threshold")
plt.plot(N_range, model.predict(X), 'r--', label=f"Nedelchev Invariant (R²={r_squared:.5f})")

plt.title("The Nedelchev Structural Law: Scale Invariance", fontsize=14)
plt.xlabel("N (Arithmetic Scale)", fontsize=12)
plt.ylabel("Critical Stability Threshold (κc)", fontsize=12)
plt.ylim(0, 2)  # Highlighting the stability at 1.0
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

# Conclusion:
# If alpha = 0 and R2 = 1, the law proves that Goldbach networks possess 
# an intrinsic, scale-independent stability threshold.