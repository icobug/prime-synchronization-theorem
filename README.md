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

* **Zenodo Archive:** [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19544373.svg)](https://doi.org/10.5281/zenodo.19544373)
* **Manuscript:** *Emergent Synchronization Dynamics in Goldbach-induced Oscillator Networks* (Currently Under Review at **Chaos, Solitons & Fractals**).

**Author:** Hristo Nedelchev  
**Status:** Independent Research / Preprint & Source Code Available
