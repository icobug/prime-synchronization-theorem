import math
import numpy as np
import matplotlib.pyplot as plt
from time import time

# --- КОНСТАНТИ ОТ ЕМПИРИЧНИЯ ЗАКОН НА НЕДЕЛЧЕВ (ОТ PDF) ---
CONSTANT_A = 2.539
EXPONENT_B = 0.9327

def sieve(n):
    """Оптимизирано сито на Ератостен за намиране на прости числа."""
    is_prime = np.ones(n + 1, dtype=bool)
    is_prime[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            is_prime[i*i : n+1 : i] = False
    return np.where(is_prime)[0]

def compute_gamma(N, primes_list, primes_set):
    """Изчислява тегловната функция Gamma(N) за дадено четно число N."""
    s = 0.0
    for p in primes_list:
        if p > N // 2:
            break
        q = N - p
        if q in primes_set:
            # Сърцето на модела: сумата от реципрочните логаритми
            s += 1.0 / (math.log(p) * math.log(q))
    return s

def kappa_c_empirical(N, gamma_val):
    """
    ИЗЧИСЛЯВА КРИТИЧНИЯ ПРАГ НА СИНХРОНИЗАЦИЯ (kappa_c) 
    чрез емпиричната формула от PDF документите.
    """
    if gamma_val == 0:
        return None
    return (CONSTANT_A * (N ** EXPONENT_B)) / gamma_val

# --- СИМУЛАЦИЯ И ТЕСТ ---
N_limit = 1000000  # Можеш да го промениш на 10 000 000 за ултра тест
num_samples = 100

print(f"--- ПЪЛЕН МОДЕЛ НА НЕДЕЛЧЕВ ---")
print(f"Използвани константи: A={CONSTANT_A}, B={EXPONENT_B}")

start_time = time()
primes = sieve(N_limit)
primes_set = set(primes)

results_N = []
results_gamma = []
results_kappa = []

test_points = np.linspace(4, N_limit, num_samples, dtype=int)
for N in test_points:
    if N % 2 != 0: N += 1
    
    g = compute_gamma(N, primes, primes_set)
    k = kappa_c_empirical(N, g)
    
    results_N.append(N)
    results_gamma.append(g)
    results_kappa.append(k)

end_time = time()
print(f"Симулацията завърши за {end_time - start_time:.2f} сек.")

# --- ВИЗУАЛИЗАЦИЯ ---
plt.figure(figsize=(14, 6))

# Първа графика: Gamma(N)
plt.subplot(1, 2, 1)
plt.scatter(results_N, results_gamma, color='blue', s=10, label='Gamma(N)')
plt.title("Goldbach Weight Function Γ(N)")
plt.xlabel("N")
plt.ylabel("Γ(N)")
plt.grid(True, alpha=0.3)

# Втора графика: Kappa_c (Емпиричната прогноза)
plt.subplot(1, 2, 2)
plt.plot(results_N, results_kappa, color='red', linewidth=2, label='Empirical κ_c')
plt.title("Predicted Synchronization Threshold κ_c")
plt.xlabel("N")
plt.ylabel("κ_c(N)")
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\nМоделът е зареден с пълните параметри от PDF доказателствата.")
