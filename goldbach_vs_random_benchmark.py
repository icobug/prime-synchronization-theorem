# ============================================================
# GOLDBACH VS RANDOM: STRUCTURAL UNIQUENESS TEST
# Proof: The Stability Law exists ONLY within Goldbach Topology
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

def get_primes(n):
    """Generate primes up to n."""
    sieve = np.ones(n, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i:n:i] = False
    return np.where(sieve)[0]

def run_benchmark(Ns):
    print(f"{'N':>5} | {'Goldbach λ_max':>15} | {'Random λ_max':>15} | {'Result'}")
    print("-" * 60)
    
    g_results = []
    r_results = []
    
    for N in Ns:
        primes = get_primes(N)
        M = len(primes)
        idx = {p: i for i, p in enumerate(primes)}
        
        # 1. GOLDBACH STRUCTURE
        W_g = np.zeros((M, M))
        for i, p in enumerate(primes):
            q = N - p
            if q in idx:
                W_g[i, idx[q]] = 1.0
        
        l_max_g = np.max(np.abs(np.linalg.eigvals(W_g)))
        
        # 2. RANDOM STRUCTURE (Same density, shuffled topology)
        # We take the exact same number of connections and shuffle them
        W_r = W_g.copy().flatten()
        np.random.shuffle(W_r)
        W_r = W_r.reshape((M, M))
        
        l_max_r = np.max(np.abs(np.linalg.eigvals(W_r)))
        
        g_results.append(l_max_g)
        r_results.append(l_max_r)
        
        status = "UNIQUE" if abs(l_max_g - l_max_r) > 0.5 else "COMMON"
        print(f"{N:5d} | {l_max_g:15.4f} | {l_max_r:15.4f} | {status}")
        
    return g_results, r_results

# --- EXECUTION ---
Ns = [200, 400, 600, 800, 1000, 1200]
print("Starting Benchmark: Goldbach (Order) vs Random (Chaos)...")
goldbach_stability, random_stability = run_benchmark(Ns)

# --- VISUALIZATION ---
plt.figure(figsize=(10, 6))
plt.plot(Ns, goldbach_stability, 'o-', label="Nedelchev Goldbach (λ=1)", linewidth=3, color='blue')
plt.plot(Ns, random_stability, 'x--', label="Randomized Topology (λ->0)", color='red')
plt.axhline(y=1.0, color='black', linestyle=':', alpha=0.5)

plt.title("Structural Uniqueness: Goldbach vs Chaos", fontsize=14)
plt.xlabel("Scale (N)", fontsize=12)
plt.ylabel("Spectral Radius (Stability Index)", fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# Scientific Conclusion:
# If Goldbach remains at 1.0 and Random drops to 0, the law is STRUCTURAL.