# Phase-Collapse (PC) Optimization Framework

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23305734.svg)](https://doi.org/10.5281/zenodo.23305734)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

**Author:** Христо Неделчев (Independent Researcher, Ruse, Bulgaria)  
**Open Science Archive:** [Zenodo DOI: 10.5281/zenodo.23305734](https://doi.org/10.5281/zenodo.23305734)

---

## Overview

Traditional metaheuristics (such as Hill Climbing, Simulated Annealing, and Genetic Algorithms) frequently fail or become trapped in sub-optimal local basins when confronted with non-smooth, discrete, multi-modal, or highly singular landscapes. 

**Phase-Collapse (PC)** is a novel hybrid metaheuristic architecture designed to navigate extreme "needle-in-a-haystack" spaces. It models the search space as a dynamic multi-phase manifold governed by rhythmic phase oscillations and structural memory.

---

## Core Architectural Pillars

1. **9-Point Phase Cycle & 10th Hyper-Transition State:**
   - **Ticks 1–9 (Breathing Phase Cycle):** Step scales vary dynamically across iterations, alternating between micro-exploration, broad expansion, and macro-leaps.
   - **Tick 10 (Hyper-Transition State):** Triggers a structural reset and multi-dimensional vector rotation to break deep regional stagnation barriers.
2. **Spatial Diversity Archive:** An elitist memory structure filtered by Manhattan distance thresholds to preserve multiple independent global/local peaks simultaneously.
3. **Micro-Scanning Beams:** Automatically activate during high-variance objective evaluations to perform high-resolution sub-grid sweeps.
4. **Adaptive Zoom & Tension Management:** Monitors stagnation counters to execute macro-teleportation between archived peaks.

---

## Repository Structure

* `phase_collapse.py` — The core optimization engine (`PhaseCollapseOptimizer`) and reference verification benchmark suite.
* `Phase-Collapse Optimization Monograph.pdf` — The comprehensive 8-page academic preprint detailing mathematical formulations and benchmark results.

---

## Installation & Quick Start

1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/phase-collapse-optimization.git](https://github.com/your-username/phase-collapse-optimization.git)
   cd phase-collapse-optimization
# Nedelchev Spectral Goldbach Proof

## Overview
This repository contains the complete research paper:  
**"Spectral Analysis of Goldbach Partitions: A Method Superior to Hardy-Littlewood"**

Based on the **Nedelchev Structural Law**:
$$κ_c = \frac{\sigma(P)}{\lambda_{\max}(P)} \sim N^\alpha, \quad \alpha \approx 0.9985$$

## Key Results
| Metric | Nedelchev Spectral | Hardy-Littlewood |
|--------|-------------------|------------------|
| DENSE Enrichment | **100.00%** | 93.33% |
| SPARSE Enrichment | **97.78%** | 6.67% |
| Correlation | **0.999978** | 0.983356 |

**Statistical Significance:**
- DENSE: t = 4.24 (p < 0.05)
- SPARSE: t = 50.21 (p < 0.001)

## Files
- `Nedelchev_Spectral_Goldbach_Proof_v2.0_Crystal_Clear.pdf` – Full paper

## Related Work
This paper extends the framework established in:  
**[Numerical Evidence for Linear Scaling Laws in Goldbach-induced Oscillator Networks](https://doi.org/10.5281/zenodo.22086177)**  
*(Zenodo, 2026)*

## Author
Hristo Nedelchev


# Emergent Synchronization Dynamics in Goldbach-induced Oscillator Networks

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19544702.svg)](https://doi.org/10.5281/zenodo.19544702)

This repository contains the official implementation and numerical evidence for the **Nedelchev Scaling Law** and the **High-Density Goldbach Bridge** in synchronization transitions within prime-induced networks.

## 🔬 Overview
We explore a fundamental link between **Analytic Number Theory** and **Statistical Physics**. By constructing network topologies based on the **Goldbach Conjecture**, we uncover a deterministic synchronization behavior that follows a robust linear scaling law and exhibits advanced spectral ordering.

### Key Discoveries:
* **The Nedelchev Scaling Law:** Numerical verification that the critical coupling strength scales linearly with system size: $\kappa_c \propto N$.
* **High-Density Synchronization ($N=400$):** Implementation of a dense informational architecture (The Nedelchev Bridge) that achieves near-perfect coherence ($R \approx 0.995$) even at large scales.
* **Spectral Radius Invariance:** We prove that the spectral radius $\rho(G)$ remains constant at 1, regardless of $N$, shifting the focus of synchronization drivers to frequency dispersion.
* **Deterministic Topology:** Unlike stochastic models, these networks are built by linking prime-indexed nodes $(p_i, p_j)$ such that $p_i + p_j = E$ for all even integers.

## 📊 Visualizing the Results

### 1. The Scaling Law
Our simulations across Kuramoto, Winfree, and Stuart-Landau models show a perfect linear fit ($R^2=1.00000$) for the synchronization threshold.



### 2. Spectral Fingerprint & Level Spacing
We provide spectral proof that Goldbach networks possess an inherent mathematical order. **Level Spacing Distribution** analysis confirms the system follows a **Poissonian regime**, distinctly separating it from the chaos of random Erdős-Rényi graphs.



### 3. The Global Bridge Effect
We identify a unique phase transition pathway, termed the **"Global Bridge"**, which describes how coherence emerges through specific arithmetic paths, suppressing the frequency entropy of prime numbers.



## 📂 Repository Structure
* **/code:** Optimized Python scripts and Jupyter Notebooks (Google Colab compatible).
    * `gold_sync_N400.py`: Large-scale synchronization engine.
    * `goldbach_spectral_tests.py`: Suite for Laplacian Eigenvalues and Poisson spacing tests.
* **/figures:** High-resolution plots of the scaling law and phase transition dynamics.
* `Universal_Synchronization_in_High_Density_Goldbach_Networks.pdf`: Technical report and theoretical framework for the $N=400$ model.

## 🚀 Getting Started
To reproduce the results, you can run the provided scripts directly:
1.  Ensure `numpy`, `scipy`, `networkx`, and `matplotlib` are installed.
2.  Run `goldbach_spectral_tests.py` to verify the mathematical order of the network.
3.  Execute the Kuramoto simulation to observe the $R=0.995$ synchronization.

## 📜 Citation & Resources
If you use this work or the Nedelchev Scaling Law in your research, please cite it as follows:

* **Zenodo Archive:** [https://doi.org/10.5281/zenodo.19544702](https://doi.org/10.5281/zenodo.19544702)
* **Manuscript:** *Emergent Synchronization Dynamics in Goldbach-induced Oscillator Networks* (Currently Under Review at **Chaos, Solitons & Fractals**).

**Author:** Hristo Nedelchev  
**Status:** Independent Research / Preprint & Source Code Available
