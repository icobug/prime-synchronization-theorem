import numpy as np
from scipy.integrate import odeint

# =================================================================
# PROJECT: ICOBUG - THE NEDELCHEV SCALING LAW
# AUTHOR: HRISTO VALENTINOV NEDELCHEV
# LICENSE: GNU GPLv3
# DESCRIPTION: Core Simulation of Goldbach Oscillator Networks
# =================================================================

def get_primes(n):
    """Sieve of Eratosthenes to generate prime frequencies."""
    primes = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes

def nedelchev_interaction_operator(primes, N):
    """Constructs the connectivity matrix W_N based on Goldbach sums."""
    M = len(primes)
    W = np.zeros((M, M))
    for i in range(M):
        for j in range(M):
            if primes[i] + primes[j] == N:
                W[i, j] = 1
    return W

def kuramoto_model(theta, t, omega, K, W, M):
    """Nedelchev-Kuramoto Dynamical Equations."""
    dtheta = np.zeros(M)
    for i in range(M):
        # The core interaction: Sum over prime partners that equal N
        interaction = np.sum(W[i, :] * np.sin(theta - theta[i]))
        dtheta[i] = omega[i] + (K / M) * interaction
    return dtheta

def run_validation(N_target=400):
    print(f"--- Running Validation for N = {N_target} ---")
    
    # 1. Prepare Prime Oscillators
    primes = get_primes(N_target)
    M = len(primes)
    omega = np.array(primes)
    
    # 2. Apply The Nedelchev Law: K = 2 * N
    K_threshold = 2 * N_target
    
    # 3. Build Topology and Check Spectral Invariance
    W = nedelchev_interaction_operator(primes, N_target)
    rho = np.max(np.abs(np.linalg.eigvals(W)))
    
    # 4. Run Dynamics (Time Evolution)
    t = np.linspace(0, 50, 1000)
    theta0 = np.random.uniform(0, 2*np.pi, M)
    sol = odeint(kuramoto_model, theta0, t, args=(omega, K_threshold, W, M))
    
    # 5. Calculate Final Order Parameter R
    final_phases = sol[-1, :]
    R = np.abs(np.mean(np.exp(1j * final_phases)))
    
    print(f"Number of Oscillators (M): {M}")
    print(f"Spectral Radius (rho): {rho:.4f} (Must be 1.0)")
    print(f"Coupling Strength (K): {K_threshold}")
    print(f"Order Parameter (R): {R:.4f} (Global Bridge achieved if > 0.9)")

if __name__ == "__main__":
    run_validation(400)