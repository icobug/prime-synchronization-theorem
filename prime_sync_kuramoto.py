"""
Goldbach Bridge Theorem - Experimental Validation
Author: Hristo Valentinov Nedelchev
Version: 3.2 (Experimental Edition)

This script simulates a Kuramoto network of prime-based oscillators 
to verify the predicted critical coupling strength (Kappa_c).
"""

import numpy as np
import matplotlib.pyplot as plt
import math

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def get_gamma(N):
    """Calculates the Goldbach weight sum from Number Theory."""
    primes = [x for x in range(2, N) if is_prime(x)]
    g_sum = sum(1.0 / (math.log(p) * math.log(N-p)) for p in primes if is_prime(N-p))
    return g_sum

def kuramoto_simulation(N, kappa):
    """Physically simulates phase-locking in the prime network."""
    dt = 0.015
    steps = 2500
    
    primes = [x for x in range(2, N) if is_prime(x)]
    n_osc = len(primes)
    if n_osc < 2: return 0
    
    # Frequency mapping (Natural frequencies = Prime numbers)
    omega = np.array(primes, dtype=float)
    phases = np.random.uniform(0, 2*np.pi, n_osc)
    
    # Vectorized simulation of the Kuramoto dynamics
    for _ in range(steps):
        phase_diffs = phases[:, None] - phases
        interaction = (kappa / n_osc) * np.sum(np.sin(phase_diffs), axis=1)
        phases += (omega + interaction) * dt
    
    # Return Order Parameter R
    return np.abs(np.mean(np.exp(1j * phases)))

# --- Execution ---
N = 500
A, B = 2.539, 0.9327 # Nedelchev Constants
gamma = get_gamma(N)
kappa_theory = (A * (N**B)) / gamma

print(f"Predicted Critical Coupling (Kappa_c): {kappa_theory:.4f}")

# Sweep through coupling strengths
kappas = np.linspace(200, 1500, 25)
R_results = [kuramoto_simulation(N, k) for k in kappas]

# Plotting the Result
plt.figure(figsize=(12, 6))
plt.plot(kappas, R_results, 'bo-', linewidth=2, label='Experimental Order Parameter (R)')
plt.axvline(x=kappa_theory, color='red', linestyle='--', linewidth=3, 
            label=f'Nedelchev Threshold ({kappa_theory:.2f})')

plt.title(f"Dynamic Synchronization Validation (N={N})", fontsize=16)
plt.xlabel("Coupling Strength (Kappa)", fontsize=14)
plt.ylabel("Order Parameter (R)", fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
