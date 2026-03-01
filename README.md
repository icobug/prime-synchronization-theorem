# Emergent Synchronization Dynamics in Goldbach-induced Oscillator Networks

![License](https://img.shields.io/badge/license-CC%20BY%204.0-blue.svg)
![Field](https://img.shields.io/badge/Field-Nonlinear%20Dynamics-orange)
![Mathematics](https://img.shields.io/badge/Math-Number%20Theory-green)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18823676.svg)](https://doi.org/10.5281/zenodo.18823676)

This repository contains the official implementation and numerical evidence for the **Nedelchev Scaling Law** in synchronization transitions within prime-induced networks.

## 🔬 Overview
We explore a fundamental link between **Analytic Number Theory** and **Statistical Physics**. By constructing network topologies based on the **Goldbach Conjecture**, we uncover a deterministic synchronization behavior that follows a robust linear scaling law.

### Key Discoveries:
* **The Nedelchev Scaling Law:** Numerical verification that the critical coupling strength scales linearly with system size: $$\kappa_c \propto N$$
* **Deterministic Topology:** Networks are built by linking prime-indexed nodes $(p_i, p_j)$ such that $p_i + p_j = N$.
* **Spectral Radius Invariance:** We prove that the spectral radius $\rho(G)$ remains constant at 1, regardless of $N$, shifting the focus of synchronization drivers to frequency dispersion.



---

## 📊 Visualizing the Results

### 1. The Scaling Law
Our simulations across Kuramoto, Winfree, and Stuart-Landau models show a perfect linear fit ($R^2 = 1.00000$) for the synchronization threshold.

### 2. The Global Bridge Effect
We identify a unique phase transition pathway, termed the **"Global Bridge"**, which describes how coherence emerges through specific arithmetic paths in Goldbach networks.

---

## 📂 Repository Structure
* `/code`: Jupyter Notebooks (.ipynb) for Google Colab.
* `/figures`: High-resolution plots and data visualizations.
* `Nedelchev_Goldbach_Synchronization_2026.pdf`: Technical preprint and theoretical framework.

## 🚀 Getting Started
To reproduce the results, you can run the provided notebooks directly in Google Colab:
1. Open the `.ipynb` files in the `/code` directory.
2. Ensure `numpy`, `scipy`, and `matplotlib` are installed.
3. Run the cells to generate the scaling law plots and synchronization animations.

## 📜 Citation & Resources
If you use this work or the Nedelchev Scaling Law in your research, please cite it as follows:

**Zenodo Archive:** [10.5281/zenodo.18823676](https://doi.org/10.5281/zenodo.18823676)  
**Manuscript:** *Emergent Synchronization Dynamics in Goldbach-induced Oscillator Networks* (Currently Under Review at *Chaos, Solitons & Fractals*).

---
**Author:** Hristo Nedelchev  
**Status:** Independent Research / Preprint Available
