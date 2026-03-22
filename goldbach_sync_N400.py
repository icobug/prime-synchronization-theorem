# =============================================================================
# ЧИСТ GOLDBACH МОДЕЛ - МНОГО ЧЕТНИ ЧИСЛА
# ЦЕЛ: N = 400
# =============================================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import sympy
import time

print("=" * 70)
print("ЧИСТ GOLDBACH МОДЕЛ - МНОГО ЧЕТНИ ЧИСЛА")
print("ЦЕЛ: СИНХРОНИЗАЦИЯ ЗА N = 400")
print("=" * 70)

# -----------------------------------------------------------------------------
# 1. ГЕНЕРИРАНЕ НА ПРОСТИТЕ ЧИСЛА
# -----------------------------------------------------------------------------
N = 400
print(f"\n📊 Генериране на първите {N} прости числа...")

primes = list(sympy.primerange(1, 3000))[:N]
omega = np.array(primes, dtype=float)
omega = omega - np.mean(omega)  # Центриране

print(f"✅ Генерирани {len(primes)} прости числа")
print(f"   Първите 5: {primes[:5]}")
print(f"   Последните 5: {primes[-5:]}")
print(f"   Честотен размах: {omega.max() - omega.min():.2f}")

# -----------------------------------------------------------------------------
# 2. ПРАВИЛНО ПОСТРОЯВАНЕ НА GOLDBACH МРЕЖАТА
# -----------------------------------------------------------------------------
print("\n" + "=" * 70)
print("ПОСТРОЯВАНЕ НА GOLDBACH МРЕЖА")
print("(използваме ВСИЧКИ четни числа от 4 до максимума)")
print("=" * 70)

# Създаваме празна матрица на съседство
A = np.zeros((N, N))
prime_to_index = {p: i for i, p in enumerate(primes)}

# Намираме всички четни числа, които можем да образуваме
max_even = primes[-1] + primes[-2]  # Най-голямото четно
min_even = 4  # Най-малкото четно

print(f"📌 Търсим Goldbach двойки за всички четни числа от {min_even} до {max_even}")

connections = 0
even_count = 0

# За всяко четно число в интервала
for E in range(min_even, max_even + 1, 2):  # Стъпка 2 (само четни)
    even_count += 1
    # Търсим двойки (p, q) такива, че p + q = E
    for i, p in enumerate(primes):
        if p > E:  # Ако p е по-голямо от E, спираме
            break
        q = E - p
        if q in prime_to_index and q >= p:  # q >= p за да избегнем дублиране
            j = prime_to_index[q]
            if i != j and A[i, j] == 0:  # Ако още няма връзка
                A[i, j] = 1
                A[j, i] = 1
                connections += 1
                
                # Показваме първите 5 примера
                if connections <= 5:
                    print(f"  Връзка {connections}: {p} + {q} = {E}")

print(f"\n📊 Проверени {even_count} четни числа")
print(f"✅ Създадени {connections} уникални връзки")

# -----------------------------------------------------------------------------
# 3. АНАЛИЗ НА МРЕЖАТА
# -----------------------------------------------------------------------------
print("\n" + "=" * 70)
print("АНАЛИЗ НА МРЕЖАТА")
print("=" * 70)

# Степен на върховете (колко връзки има всеки възел)
degrees = np.sum(A, axis=1)
print(f"📊 Степен на върховете:")
print(f"   Минимална степен: {degrees.min()}")
print(f"   Максимална степен: {degrees.max()}")
print(f"   Средна степен: {degrees.mean():.2f}")

# Спектрален радиус
eigenvalues = np.linalg.eigvalsh(A)
spectral_radius = np.max(np.abs(eigenvalues))
print(f"\n📊 Спектрален радиус: {spectral_radius:.6f}")

# Проверка дали мрежата е свързана
from scipy.sparse.csgraph import connected_components
n_components, labels = connected_components(A, directed=False)
print(f"📊 Брой свързани компоненти: {n_components}")

if n_components == 1:
    print("✅ Мрежата е напълно свързана!")
else:
    print(f"⚠️ Мрежата има {n_components} отделни компоненти")

# -----------------------------------------------------------------------------
# 4. ДЕФИНИРАНЕ НА KURAMOTO МОДЕЛА
# -----------------------------------------------------------------------------
print("\n" + "=" * 70)
print("ДЕФИНИРАНЕ НА KURAMOTO МОДЕЛА")
print("=" * 70)

def kuramoto_derivative(t, theta, omega, A, kappa):
    N = len(theta)
    theta_i = theta[:, np.newaxis]
    theta_j = theta[np.newaxis, :]
    phase_diff = theta_j - theta_i
    interaction = A * np.sin(phase_diff)
    sum_over_j = np.sum(interaction, axis=1)
    return omega + kappa * sum_over_j

def order_parameter(theta):
    complex_sum = np.sum(np.exp(1j * theta))
    return np.abs(complex_sum) / len(theta)

print("✅ Моделът е дефиниран")

# -----------------------------------------------------------------------------
# 5. ТЕСТВАНЕ НА РАЗЛИЧНИ KAPPA
# -----------------------------------------------------------------------------
print("\n" + "=" * 70)
print("ТЕСТВАНЕ НА РАЗЛИЧНИ KAPPA")
print("=" * 70)

# По-малки kappa, защото вече имаме много връзки
kappa_values = [100, 200, 400, 800, 1600]
results = []

# Начални условия
np.random.seed(42)
theta0 = np.random.uniform(-np.pi, np.pi, N)

# Времеви интервал (по-кратък за по-бързо тестване)
t_span = (0, 20)
t_eval = np.linspace(0, 20, 50)

print(f"\nТестваме kappa стойности: {kappa_values}")
print("-" * 50)

for kappa in kappa_values:
    print(f"\n🔧 Тестване kappa = {kappa}")
    start = time.time()
    
    try:
        solution = solve_ivp(
            kuramoto_derivative,
            t_span,
            theta0,
            args=(omega, A, kappa),
            method='DOP853',
            t_eval=t_eval,
            rtol=1e-3,
            atol=1e-5
        )
        
        theta_t = solution.y
        R_t = np.array([order_parameter(theta_t[:, i]) for i in range(len(t_eval))])
        final_R = R_t[-1]
        
        elapsed = time.time() - start
        print(f"   Краен R: {final_R:.4f}")
        print(f"   Време: {elapsed:.1f} сек")
        
        results.append({'kappa': kappa, 'R': final_R})
        
    except Exception as e:
        print(f"   ❌ Грешка: {e}")
        results.append({'kappa': kappa, 'R': 0})

# -----------------------------------------------------------------------------
# 6. РЕЗУЛТАТИ
# -----------------------------------------------------------------------------
print("\n" + "=" * 70)
print("РЕЗУЛТАТИ")
print("=" * 70)
print(f"\n{'Kappa':<10} {'Краен R':<12} {'Статус':<15}")
print("-" * 40)

for r in results:
    status = "✅ СИНХР." if r['R'] > 0.9 else "❌ НЕ"
    print(f"{r['kappa']:<10} {r['R']:<12.4f} {status}")

# Намираме критичното kappa
for r in results:
    if r['R'] > 0.9:
        print(f"\n🎯 КРИТИЧНО kappa_c ≈ {r['kappa']}")
        print(f"   Съотношение kappa_c / N = {r['kappa']/N:.2f}")
        break
else:
    print(f"\n⚠️ Няма синхронизация до kappa = {kappa_values[-1]}")
    print(f"   Нужно е по-голямо kappa")

# -----------------------------------------------------------------------------
# 7. ВИЗУАЛИЗАЦИЯ
# -----------------------------------------------------------------------------
print("\n" + "=" * 70)
print("ВИЗУАЛИЗАЦИЯ")
print("=" * 70)

plt.figure(figsize=(15, 10))

# Графика 1: Разпределение на степените
plt.subplot(2, 2, 1)
plt.hist(degrees, bins=30, edgecolor='black')
plt.xlabel('Степен на върховете (брой връзки)')
plt.ylabel('Брой върхове')
plt.title('Фиг. 1: Разпределение на степените в Goldbach мрежата')
plt.grid(True, alpha=0.3)

# Графика 2: Спектър
plt.subplot(2, 2, 2)
non_zero_eigs = eigenvalues[np.abs(eigenvalues) > 1e-10]
plt.stem(non_zero_eigs, markerfmt='ro', linefmt='r-', basefmt=' ')
plt.xlabel('Индекс')
plt.ylabel('Собствена стойност')
plt.title('Фиг. 2: Спектър на Goldbach матрицата')
plt.grid(True, alpha=0.3)
plt.ylim(-1.1, max(1.1, non_zero_eigs.max()*1.1))

# Графика 3: Резултати от тестовете
plt.subplot(2, 2, 3)
kappas = [r['kappa'] for r in results]
Rs = [r['R'] for r in results]
plt.plot(kappas, Rs, 'bo-', linewidth=2, markersize=8)
plt.xlabel('Kappa (сила на връзката)')
plt.ylabel('Краен R (параметър на реда)')
plt.title('Фиг. 3: Преход към синхронизация')
plt.grid(True, alpha=0.3)
plt.axhline(y=0.9, color='r', linestyle='--', label='Праг на синхронизация')
plt.xscale('log')
plt.legend()

# Графика 4: Визуализация на мрежата (част от нея)
plt.subplot(2, 2, 4)
# Показваме малка част от матрицата за прегледност
plt.spy(A[:50, :50], markersize=2)
plt.xlabel('Възел индекс')
plt.ylabel('Възел индекс')
plt.title('Фиг. 4: Структура на Goldbach мрежата (първите 50 върха)')

plt.tight_layout()
plt.show()

print("\n" + "=" * 70)
print("ТЕСТЪТ ЗАВЪРШИ")
print("=" * 70)