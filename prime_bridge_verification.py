"""
PROJECT: The Prime Synchronization Theorem
AUTHOR: Hristo Nedelchev
DESCRIPTION: This script visualizes the 'Goldbach Bridge' and extracts the 
spectral properties (lambda_2 and lambda_max) used in Theorem 1 to 
predict physical synchronization thresholds.
"""

import networkx as nx
import matplotlib.pyplot as plt
from sympy import primerange
import numpy as np

def generate_goldbach_bridge(n_limit):
    # 1. Генериране на прости числа до N
    primes = list(primerange(2, n_limit + 1))
    
    # 2. Създаване на граф
    # Възлите са четните числа (целите на Голдбах)
    G = nx.Graph()
    even_numbers = list(range(4, n_limit + 1, 2))
    G.add_nodes_from(even_numbers)

    # 3. Изграждане на "Моста" (The Bridge)
    # Свързваме четно число n с простите числа p и q, ако n = p + q
    for n in even_numbers:
        for p in primes:
            if p < n:
                q = n - p
                if q in primes:
                    # Добавяме връзка между четното число и неговите съставители
                    G.add_edge(n, p)
                    G.add_edge(n, q)

    return G

# Параметри за визуализация
N = 30  # Мащабът, предложен за експериментална верификация
bridge_graph = generate_goldbach_bridge(N)

# Изчисляване на Спектралните свойства на Лапласовата матрица (Theorem 1)
# Тези стойности определят стабилността на синхронизацията във физиката
laplacian_matrix = nx.laplacian_matrix(bridge_graph).todense()
eigenvalues = sorted(np.linalg.eigvals(laplacian_matrix).real)

# Филтрираме нулевата собствена стойност (винаги първа в Лапласиан)
lambda_2 = eigenvalues[1] if len(eigenvalues) > 1 else 0
lambda_max = eigenvalues[-1]

print(f"--- Prime Synchronization Bridge Verification (N={N}) ---")
print(f"Алгебрична свързаност (λ2): {lambda_2:.4f}")
print(f"Спектрален радиус (λ_max): {lambda_max:.4f}")
print(f"Компонент на формулата Kc(N) ~ {lambda_max/lambda_2:.4f} (при λ2 > 0)")
print("-" * 55)

# Визуализация на мрежовата структура

plt.figure(figsize=(12, 8))
pos = nx.kamada_kawai_layout(bridge_graph) # По-добра подредба за спектрални графи

# Рисуване на възлите и връзките
nx.draw_networkx_nodes(bridge_graph, pos, node_color='gold', node_size=600)
nx.draw_networkx_labels(bridge_graph, pos, font_size=10, font_weight='bold')
nx.draw_networkx_edges(bridge_graph, pos, edge_color='skyblue', alpha=0.6)

plt.title(f"Goldbach Bridge Graph (N={N})\nSpectral validation for Prime Synchronization Theorem")
plt.axis('off')
plt.show()