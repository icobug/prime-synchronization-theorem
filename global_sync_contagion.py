import numpy as np
import matplotlib.pyplot as plt

def run_contagion_experiment(N_target=800):
    primes = [p for p in range(2, N_target) if all(p % i != 0 for i in range(2, int(p**0.5) + 1))]
    M = len(primes)
    omega = np.array(primes, dtype=float)
    theta = np.random.uniform(0, 2*np.pi, M)
    dt, steps = 0.02, 1500
    
    W = np.zeros((M, M))
    primes_idx = {p: i for i, p in enumerate(primes)}
    for i, p in enumerate(primes):
        q = N_target - p
        if q in primes_idx:
            W[i, primes_idx[q]] = 15.0 

    R_history = []
    for t in range(steps):
        order_param = np.mean(np.exp(1j * theta))
        R = np.abs(order_param)
        phi = np.angle(order_param)
        diff = theta[:, None] - theta
        bridge_force = np.sum(W * np.sin(diff), axis=1)
        infection_force = 3.0 * R * np.sin(phi - theta)
        theta += (omega - 0.5 * bridge_force + infection_force) * dt
        R_history.append(R)
    return R_history

history = run_contagion_experiment()
plt.figure(figsize=(10, 5))
plt.plot(history, color='magenta', label='Global Sync (R)')
plt.title("Contagion Test: From Local Pairs to Global Rhythm")
plt.xlabel("Steps")
plt.ylabel("R")
plt.grid(True, alpha=0.3)
plt.show()