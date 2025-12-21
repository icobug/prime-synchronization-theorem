"""
Prime Synchronization Theorem - Main Simulation
Simulates the prime-coupled Kuramoto oscillator system.
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import laplacian
import networkx as nx
import matplotlib.pyplot as plt
from sympy import isprime
import warnings
warnings.filterwarnings('ignore')

class PrimeSynchronization:
    """Simulates the prime-coupled oscillator system."""
    
    def __init__(self, N=30):
        """
        Initialize system for even N.
        
        Parameters:
        -----------
        N : int
            Even integer >= 4, defines the Goldbach sum
        """
        if N % 2 != 0 or N < 4:
            raise ValueError("N must be even and >= 4")
        
        self.N = N
        self.primes = self._get_primes(N)
        self.m = len(self.primes)
        self.frequencies = np.log(self.primes)
        self.adjacency = self._build_goldbach_graph()
        self.degrees = self.adjacency.sum(axis=1)
        self.avg_degree = np.mean(self.degrees)
        
        print(f"System initialized for N={N}")
        print(f"  Primes: {self.primes}")
        print(f"  Number of oscillators: {self.m}")
        print(f"  Goldbach pairs: {int(np.sum(self.adjacency)/2)}")
    
    def _get_primes(self, n):
        """Return list of primes <= n."""
        return [p for p in range(2, n+1) if isprime(p)]
    
    def _build_goldbach_graph(self):
        """Build adjacency matrix for Goldbach graph."""
        n_primes = len(self.primes)
        adj = np.zeros((n_primes, n_primes), dtype=int)
        
        # Create mapping from prime to index
        prime_to_idx = {p: i for i, p in enumerate(self.primes)}
        
        # Find Goldbach pairs
        for i, p in enumerate(self.primes):
            for j, q in enumerate(self.primes[i:], i):
                if p + q == self.N:
                    adj[i, j] = 1
                    adj[j, i] = 1
        
        return adj
    
    def kuramoto_ode(self, t, theta, kappa):
        """Kuramoto ODE for the system."""
        dtheta = np.zeros_like(theta)
        
        for i in range(self.m):
            # Natural frequency term
            dtheta[i] = self.frequencies[i]
            
            # Coupling term (only with Goldbach pairs)
            for j in range(self.m):
                if self.adjacency[i, j]:
                    dtheta[i] += (kappa / self.avg_degree) * np.sin(theta[j] - theta[i])
        
        return dtheta
    
    def simulate(self, kappa, t_span=(0, 100), initial_phases=None):
        """
        Simulate system for given coupling strength.
        
        Returns:
        --------
        sol : OdeSolution
            Solution object from solve_ivp
        """
        if initial_phases is None:
            initial_phases = 2 * np.pi * np.random.rand(self.m)
        
        # Solve ODE
        sol = solve_ivp(
            fun=lambda t, y: self.kuramoto_ode(t, y, kappa),
            t_span=t_span,
            y0=initial_phases,
            method='RK45',
            rtol=1e-8,
            atol=1e-10
        )
        
        return sol
    
    def order_parameter(self, theta):
        """Calculate synchronization order parameter."""
        return np.abs(np.sum(np.exp(1j * theta))) / len(theta)
    
    def find_critical_kappa(self, kappa_range=(0, 1000), tol=1.0):
        """
        Find critical coupling strength via binary search.
        
        Returns:
        --------
        kappa_c : float
            Estimated critical coupling
        """
        kappa_low, kappa_high = kappa_range
        
        for _ in range(20):  # Max 20 iterations
            kappa_mid = (kappa_low + kappa_high) / 2
            
            # Simulate and check synchronization
            sol = self.simulate(kappa_mid, t_span=(0, 200))
            r_final = self.order_parameter(sol.y[:, -1])
            
            if r_final > 0.7:  # Synchronized
                kappa_high = kappa_mid
            else:  # Not synchronized
                kappa_low = kappa_mid
            
            if kappa_high - kappa_low < tol:
                break
        
        return (kappa_low + kappa_high) / 2

def main():
    """Example usage and demonstration."""
    print("=" * 60)
    print("PRIME SYNCHRONIZATION THEOREM - SIMULATION")
    print("=" * 60)
    
    # Create system for N=30
    system = PrimeSynchronization(N=30)
    
    # Find critical coupling
    print("\nFinding critical coupling κ_c...")
    kappa_c = system.find_critical_kappa()
    print(f"  Estimated κ_c(30) = {kappa_c:.2f}")
    print(f"  Theoretical value ≈ 174.2")
    
    # Simulate below and above critical coupling
    print("\nSimulating system dynamics:")
    
    kappas = [50, 174.2, 300]  # Subcritical, critical, supercritical
    results = []
    
    for kappa in kappas:
        sol = system.simulate(kappa, t_span=(0, 150))
        r_final = system.order_parameter(sol.y[:, -1])
        results.append((kappa, r_final))
        
        status = "SYNCHRONIZED" if r_final > 0.7 else "NOT SYNCHRONIZED"
        print(f"  κ = {kappa:6.1f} → r = {r_final:.3f} ({status})")
    
    # Create visualization
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Plot 1: Phase evolution for critical kappa
    sol_critical = system.simulate(kappa_c, t_span=(0, 100))
    for i in range(min(5, system.m)):  # Plot first 5 oscillators
        axes[0].plot(sol_critical.t, sol_critical.y[i], label=f'p={system.primes[i]}')
    axes[0].set_xlabel('Time (τ)')
    axes[0].set_ylabel('Phase Θ')
    axes[0].set_title(f'Phase Evolution for κ = {kappa_c:.1f}')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # Plot 2: Order parameter vs kappa
    test_kappas = np.linspace(0, 350, 20)
    r_values = []
    for k in test_kappas:
        sol = system.simulate(k, t_span=(0, 100))
        r_values.append(system.order_parameter(sol.y[:, -1]))
    
    axes[1].plot(test_kappas, r_values, 'b-o', linewidth=2, markersize=6)
    axes[1].axvline(x=kappa_c, color='r', linestyle='--', label=f'κ_c = {kappa_c:.1f}')
    axes[1].set_xlabel('Coupling Strength (κ)')
    axes[1].set_ylabel('Order Parameter (r)')
    axes[1].set_title('Synchronization Transition')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('synchronization_results.png', dpi=150)
    plt.show()
    
    print("\n" + "=" * 60)
    print(f"Simulation complete. Results saved to 'synchronization_results.png'")
    print("=" * 60)

if __name__ == "__main__":
    main()
