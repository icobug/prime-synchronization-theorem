"""
=============================================================================
PHASE-COLLAPSE OPTIMIZATION FRAMEWORK (CORE ALGORITHM & SUITE)
=============================================================================
Author: Христо Неделчев (Independent Researcher, Ruse, Bulgaria)
License: MIT Open Source License
Description: A hybrid metaheuristic architecture combining Phase-Cycle Movement, 
Spatial Diversity Archives, Micro-Scanning Beams, and Adaptive Zoom for 
non-smooth, multi-modal, and chaotic landscapes.
=============================================================================
"""

import numpy as np

class PhaseCollapseOptimizer:
    """
    Core Phase-Collapse Optimization Engine.
    Handles the 9-point phase cycle, 10th hyper-transition state, spatial archive,
    and micro-scanning beams for extreme non-smooth landscapes.
    """
    def __init__(self, bounds, dim=1, seed=2026):
        self.bounds = bounds  # List of (min, max) tuples for each dimension
        self.dim = dim
        np.random.seed(seed)
        self.archive = []
        
    def update_archive(self, position, value):
        """
        Spatial Diversity Archive with Manhattan distance filtering to preserve
        multiple independent global/local peaks without premature convergence.
        """
        pos_arr = np.array(position)
        span = self.bounds[0][1] - self.bounds[0][0]
        for p in self.archive:
            dist = np.sum(np.abs(p['pos'] - pos_arr))
            if dist < 0.1 * self.dim * span:
                if value > p['val']:
                    self.archive.remove(p)
                    break
                else:
                    return
        self.archive.append({'pos': pos_arr, 'val': value})
        self.archive.sort(key=lambda x: x['val'], reverse=True)
        if len(self.archive) > 5:
            self.archive.pop()

    def optimize(self, objective_func, iterations=3500):
        """
        Executes the optimization loop:
        - Ticks 1-9: Breathing Phase Cycle (dynamic step scaling)
        - Tick 10: Hyper-Transition State (structural reset & archive recall)
        - Micro-scanning beams & tension management
        """
        curr_pos = np.array([np.random.uniform(b[0], b[1]) for b in self.bounds])
        curr_val = objective_func(curr_pos)
        self.update_archive(curr_pos, curr_val)
        
        best = self.archive[0]
        tension = 0.0
        stagnation = 0
        
        span = self.bounds[0][1] - self.bounds[0][0]
        
        for t in range(1, iterations + 1):
            # 9-point phase cycle with 10th hyper-transition state
            phase_cycle = (t % 10) + 1  
            step_scale = max(0.01, (phase_cycle / 10.0) * span * 0.1)
            
            # Perturbation & Movement
            delta = np.random.normal(0, step_scale, self.dim)
            curr_pos = np.clip(curr_pos + delta, [b[0] for b in self.bounds], [b[1] for b in self.bounds])
            
            val = objective_func(curr_pos)
            
            if val > best['val']:
                best = {'pos': curr_pos.copy(), 'val': val}
                tension = 0.0
                stagnation = 0
            else:
                tension += 1.0
                stagnation += 1
                
            self.update_archive(curr_pos, val)
            best = self.archive[0]
            
            # Stagnation escape via 10th-tick hyper-transition / macro-teleportation
            if stagnation > 15 or tension > 5.0 or phase_cycle == 10:
                if len(self.archive) > 1 and np.random.rand() > 0.2:
                    chosen = self.archive[np.random.choice(len(self.archive))]
                    curr_pos = chosen['pos'] + np.random.normal(0, step_scale * 0.5, self.dim)
                else:
                    curr_pos = np.array([np.random.uniform(b[0], b[1]) for b in self.bounds])
                stagnation = 0
                tension = 0.0
                
        return best['pos'], best['val'], self.archive


# =============================================================================
# OPTIONAL BENCHMARK SUITE (For verification and demonstration)
# =============================================================================
def benchmark_hyperchaos_2d(params):
    K, gamma = params
    dt = 0.005
    steps = 200
    s1 = np.array([1.2, 0.8, 1.0, 0.5])
    s2 = np.array([0.5, 1.5, 0.8, 1.2])
    
    error_history = []
    for _ in range(steps):
        dx1 = 35.0 * (s1[1] - s1[0]) + s1[3]
        dy1 = 12.0 * s1[0] - s1[1] - s1[0] * s1[2]
        dz1 = s1[0] * s1[1] - 3.0 * s1[2]
        dw1 = -s1[1] * s1[2] + gamma * s1[3]
        s1 += np.array([dx1, dy1, dz1, dw1]) * dt
        
        dx2 = 35.0 * (s2[1] - s2[0]) + s2[3] + K * (s1[0] - s2[0])
        dy2 = 12.0 * s2[0] - s2[1] - s2[0] * s2[2] + K * (s1[1] - s2[1])
        dz2 = s2[0] * s2[1] - 3.0 * s2[2] + K * (s1[2] - s2[2])
        dw2 = -s2[1] * s2[2] + gamma * s2[3] + K * (s1[3] - s2[3])
        s2 += np.array([dx2, dy2, dz2, dw2]) * dt
        error_history.append(np.linalg.norm(s1 - s2))
        
    steady_errors = np.array(error_history[100:])
    return np.var(steady_errors) * 100.0


if __name__ == "__main__":
    print("Executing Phase-Collapse Optimizer verification...")
    optimizer = PhaseCollapseOptimizer(bounds=[(0.5, 15.0), (0.1, 5.0)], dim=2, seed=2026)
    best_pos, best_val, _ = optimizer.optimize(benchmark_hyperchaos_2d, iterations=1500)
    print(f"Optimal Parameters -> K: {best_pos[0]:.2f}, Gamma: {best_pos[1]:.2f} | Value: {best_val:.2f}")