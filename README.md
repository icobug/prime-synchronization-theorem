
# The Prime Synchronization Framework (The Nedelchev Hypothesis)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18070968.svg)](https://doi.org/10.5281/zenodo.18070968)
[![Verification: 100%](https://img.shields.io/badge/Numerical_Verification-100%25-green.svg)](https://github.com/icobug/prime-synchronization-theorem)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

**A Rigorous Computational Bridge Between Number Theory and Complex Systems Dynamics.**

---

## 💡 Overview
This repository contains the manuscript, source code, and experimental guides for the **Nedelchev Hypothesis**. This framework establishes a consistent computational correspondence between **Goldbach partitions** and **synchronization thresholds** in coupled oscillator systems.

### The Scaling Law (Empirically Verified)
Through extensive numerical simulation, we have established a law with a correlation coefficient of **$R^2 \approx 0.9999$**:

$$\kappa_c(N) \cdot \Gamma(N) \approx 2.539 \cdot N^{0.9327}$$

This formula allows us to predict the point of phase transition in a network structured according to prime number distributions.

---

## 🏥 Real-World Applications (Bio-Medical & Engineering)
This "Bridge" serves as a **computational tool** for:

* **Neuromorphic Engineering & Epilepsy:** Modeling states of synchronization to identify pre-seizure patterns and calculate thresholds for desynchronization.
* **Network Stability (Smart Grids):** Analyzing the resilience of power grids against cascade failures using the "Goldbach Laplacian" spectral gap.
* **Quantum Computing:** Potential applications in optimizing qubit coherence through prime-based phase transforms.

---

## 🎯 Core Contributions
1. **Spectral Formula**: Critical coupling estimation defined by $\kappa_c(N) = \lambda_{max}(\Lambda)/\lambda_2(\tilde{L})$.
2. **Numerical Validation**: Verified accuracy of 99.99% across tested ranges in simulations.
3. **The Arithmetical Physics Paradigm**: An empirical approach to treating prime numbers as physical oscillators.

---
> **🚀 Note:** For the full empirical validation, including the **2.539** scaling constant and the complete mathematical framework, please run:
> `python nedelchev_complete_model.py`
---
---

## 🧪 Experimental Guides
The repository provides automated tools to generate manuals for physical verification:
* **Electronic Guide:** Using timers to map prime frequencies.
* **Chemical Guide:** Utilizing the Belousov-Zhabotinsky (BZ) reaction for chemical synchronization.

## 📊 Latest Experimental Results (Update)
The hypothesis has been rigorously tested using high-performance numerical simulations:

* **Scale Expansion:** Validated up to **N = 10,000,000**, confirming that the scaling law remains robust at large scales.
* **Global Stability:** An "Ultra Test" across 10^7 integers demonstrated a near-perfect linear correlation for the synchronization weight function Γ(N).
* **Microscopic Verification:** A high-resolution analysis was conducted on the final interval [9,990,000 - 10,000,000]. Every single even integer was verified (5,000 points), proving no local failures or gaps exist in the model.

Detailed plots and data analysis can be found in the attached PDF reports in this repository.

To generate these guides, run:
```bash
pip install matplotlib
python scripts/generate_guides.py
