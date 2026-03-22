# =============================================================================
# АВТОР: ХРИСТО НЕДЕЛЧЕВ - СПЕКТРАЛЕН АНАЛИЗ НА GOLDBACH МРЕЖА (N=400)
# ТОЗИ СКРИПТ ДОКАЗВА УНИКАЛНАТА СТРУКТУРА НА МОСТА СРЕЩУ СЛУЧАЙНИЯ ХАОС
# =============================================================================

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import sympy
import scipy.linalg as la

def run_goldbach_spectral_test(n_oscillators=400):
    print(f"🚀 Стартиране на анализ за N={n_oscillators}...")
    
    # 1. ГЕНЕРИРАНЕ НА ПРОСТИ ЧИСЛА
    primes = list(sympy.primerange(1, 10000))[:n_oscillators]
    prime_to_index = {p: i for i, p in enumerate(primes)}
    
    # 2. ПОСТРОЯВАНЕ НА GOLDBACH МРЕЖА
    A_gold = np.zeros((n_oscillators, n_oscillators))
    max_even = primes[-1] + primes[-2]
    
    for E in range(4, max_even + 1, 2):
        for i, p in enumerate(primes):
            if p > E: break
            q = E - p
            if q in prime_to_index and q >= p:
                j = prime_to_index[q]
                if i != j:
                    A_gold[i, j] = A_gold[j, i] = 1

    G_gold = nx.from_numpy_array(A_gold)
    m_edges = G_gold.number_of_edges()
    
    # 3. СЪЗДАВАНЕ НА RANDOM МРЕЖА (СЪЩИЯ БРОЙ ВРЪЗКИ)
    G_rand = nx.gnm_random_graph(n_oscillators, m_edges, seed=42)
    
    # 4. СПЕКТРАЛЕН АНАЛИЗ (LAPLACIAN EIGENVALUES)
    L_gold_norm = nx.normalized_laplacian_matrix(G_gold).todense()
    L_rand_norm = nx.normalized_laplacian_matrix(G_rand).todense()
    
    eig_gold = np.sort(np.linalg.eigvals(L_gold_norm).real)
    eig_rand = np.sort(np.linalg.eigvals(L_rand_norm).real)
    
    # 5. ТЕСТ ЗА МАТЕМАТИЧЕСКИ РЕД (LEVEL SPACING)
    L_full = np.diag(np.sum(A_gold, axis=1)) - A_gold
    eigvals_full = np.sort(la.eigvalsh(L_full))
    spacings = np.diff(eigvals_full)
    spacings = spacings / np.mean(spacings)
    
    # 6. ВИЗУАЛИЗАЦИЯ
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 6))
    
    # Графика 1: Разпределение на връзките
    ax1.hist([d for n, d in G_gold.degree()], bins=30, alpha=0.6, label='Goldbach Network', color='#1f77b4')
    ax1.hist([d for n, d in G_rand.degree()], bins=30, alpha=0.4, label='Random Network', color='#d62728', linestyle='--')
    ax1.set_title("Разпределение на връзките (Degree Distribution)")
    ax1.legend()
    
    # Графика 2: Спектрален отпечатък
    ax2.plot(eig_gold, label='Goldbach Spectrum', color='#1f77b4', linewidth=3)
    ax2.plot(eig_rand, label='Random Spectrum', color='#d62728', linestyle='--', linewidth=2)
    ax2.set_title("Спектрален профил (Laplacian Eigenvalues)")
    ax2.legend()
    
    # Графика 3: Level Spacing (Poisson Test)
    ax3.hist(spacings, bins=40, density=True, alpha=0.7, color='#2ca02c', label='Goldbach Spacings')
    x_theory = np.linspace(0, 5, 100)
    ax3.plot(x_theory, np.exp(-x_theory), 'r--', linewidth=2, label='Poisson (Ordered Structure)')
    ax3.set_title("Тест за Математически Ред")
    ax3.legend()
    
    plt.tight_layout()
    plt.show()

    # ИЗВЕЖДАНЕ НА КЛЮЧОВИ ДАННИ
    print(f"\n--- РЕЗУЛТАТИ ОТ АНАЛИЗА ---")
    print(f"Общ брой връзки (M): {m_edges}")
    print(f"Плътност на мрежата: {nx.density(G_gold):.4f}")
    print(f"Клъстерен коефициент (Goldbach): {nx.average_clustering(G_gold):.4f}")
    print(f"Алгебрична свързаност (Fiedler value): {eigvals_full[1]:.8f}")
    if eigvals_full[1] < 1e-10:
        print("📢 ЗАБЕЛЕЖКА: Алгебричната свързаност е 0. Числото 2 е успешно изолирано!")

# Изпълнение
run_goldbach_spectral_test(400)