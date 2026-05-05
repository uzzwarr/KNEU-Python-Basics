"""
лабораторна робота №2_2. numpy (розширені завдання) — варіант 9
параметри: a=4, n=4, m=5, start=-15, end=15, step=1
seed: np.random.RandomState(96)
f(x): sin(bx) при x<5; sqrt(|bx+5|) при 5<x<7; ln(x+b) при x>7
      b=2, при x=7 функція не визначена
big_array — 10 000 рівновіддалених точок з (-20, 25)
"""

import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

import numpy as np
import time

rng = np.random.RandomState(96)
a, n, m = 4, 4, 5
start, end, step = -15, 15, 1
b = 2

# відтворення послідовності rng (той самий порядок що в lr2_1)
pool_x = np.arange(-10, 6, 2)
x  = rng.choice(pool_x, size=16)
y  = rng.uniform(0, 1, size=16)
_  = rng.uniform(-m, m, size=(n, m))
_  = np.round(rng.uniform(0, 1, size=(n, m)), 2)
_  = rng.choice(np.arange(-n+1, n, 2), size=(n, m, 3))
pool_A = np.arange(start, end+1, step)
A  = rng.choice(pool_A, size=(6, 6))

z  = np.arange(6) + a
print("=" * 60)
print("матриця A (6x6):"); print(A)
print(f"\nвектор z = {z}")

print("\n" + "=" * 60)
print("завдання 1. аналіз елементів матриці A")
print("=" * 60)

# 1a — унікальні елементи
unique_A = np.unique(A)
print(f"\n1a) унікальні ({len(unique_A)} шт.): {unique_A}")

# 1b — три найбільших по кожному рядку
print("\n1b) три найбільших по рядках:")
for i, row in enumerate(A):
    print(f"  рядок {i}: {np.sort(row)[-3:][::-1]}")

# 1c — спільні елементи стовпців 0 та 1
common = sorted(set(A[:,0]) & set(A[:,1]))
print(f"\n1c) спільні елементи стовпців 0 і 1: {common}")

# 1d — кількість ненульових та їх сума
print(f"\n1d) ненульових: {np.count_nonzero(A)}, сума: {A[A!=0].sum()}")

print("\n" + "=" * 60)
print("завдання 2. лінійна алгебра")
print("=" * 60)

# 2a — Az
print(f"\n2a) Az = {A @ z}")

# 2b — обернена
try:
    print(f"\n2b) A^(-1):\n{np.round(np.linalg.inv(A), 4)}")
except np.linalg.LinAlgError:
    print("\n2b) матриця вироджена")

# 2c — норми
print(f"\n2c) A: L1={np.round(np.linalg.norm(A,ord=1),4)}, L2={np.round(np.linalg.norm(A,ord=2),4)}")
print(f"    z: L1={np.linalg.norm(z,ord=1)}, L2={np.round(np.linalg.norm(z),4)}")

# 2d — власні значення
evals, evecs = np.linalg.eig(A)
print(f"\n2d) власні значення: {np.round(evals, 3)}")

# 2e — ранг та детермінант
print(f"\n2e) ранг={np.linalg.matrix_rank(A)}, det={np.round(np.linalg.det(A),4)}")

# 2f — слід та діагональ
print(f"\n2f) слід={np.trace(A)}, діагональ={np.diag(A)}")

# 2g — SVD та QR
U, S, Vt = np.linalg.svd(A)
Q, R = np.linalg.qr(A)
print(f"\n2g) SVD сингулярні значення: {np.round(S,4)}")
print(f"    QR матриця R:\n{np.round(R,4)}")

print("\n" + "=" * 60)
print("завдання 3. тривимірний масив B")
print("=" * 60)

B = rng.choice(pool_A, size=(n, m, 3))
print(f"\nB форма {B.shape}")

# 3a — сума по осі 2
print(f"\n3a) сума axis=2:\n{B.sum(axis=2)}")

# 3b — індекс max
idx = np.unravel_index(B.argmax(), B.shape)
print(f"\n3b) max={B.max()}, індекс {idx}")

# 3c — транспонування осей 0↔1
B_t = B.transpose(1, 0, 2)
print(f"\n3c) форма після transpose(1,0,2): {B.shape} → {B_t.shape}")

# 3d — вектор-рядок
B_flat = B.flatten()
print(f"\n3d) flatten: {len(B_flat)} елементів, перші 10: {B_flat[:10]}")

print("\n" + "=" * 60)
print("завдання 4. arr n*m з булевими масками")
print("=" * 60)

arr = rng.choice(pool_A, size=(n, m))
print(f"\narr ({n}x{m}):\n{arr}")

# 4a — додатні
print(f"\n4a) додатні: {arr[arr > 0]}")

# 4b — додатні кратні 3
mask_b = (arr > 0) & (arr % 3 == 0)
print(f"4b) додатні кратні 3: {arr[mask_b]}")

# 4c — від'ємні → -1
arr_c = arr.copy(); arr_c[arr_c < 0] = -1
print(f"\n4c) від'ємні → -1:\n{arr_c}")

# 4d — fancy indexing
print(f"\n4d) [(3,0),(0,2),(2,1)]: {arr[[3,0,2],[0,2,1]]}")

# 4e — np.ix_ регіон
region = arr[np.ix_([3,0],[1,0,3,2])]
print(f"\n4e) регіон рядки[3,0] × стовпці[1,0,3,2]:\n{region}")

print("\n" + "=" * 60)
print("завдання 5. arr1, arr2 та схожість")
print("=" * 60)

arr1 = arr.flatten().astype(float)
arr2 = arr1 + rng.random(len(arr1))
print(f"\narr1: {arr1}")
print(f"arr2: {np.round(arr2, 4)}")

# відносне відхилення
rel = np.abs(arr2 - arr1) / (np.abs(arr1) + 1e-10)

print(f"\n5c) допуск 5%: в цілому={bool(np.all(rel<=0.05))}")
print(f"    поелементно: {rel<=0.05}")
print(f"    допуск 1%: в цілому={bool(np.all(rel<=0.01))}")
print(f"    поелементно: {rel<=0.01}")

ok_1 = rel <= 0.01

# 5d-i булева маска
arr2_mask = arr2.copy()
arr2_mask[~ok_1] = arr1[~ok_1]
print(f"\n5d-i)  маска:    {np.round(arr2_mask, 4)}")

# 5d-ii np.where
arr2_where = np.where(ok_1, arr2, arr1)
print(f"5d-ii) np.where: {np.round(arr2_where, 4)}")
print(f"  однакові: {np.allclose(arr2_mask, arr2_where)}")

print("\n" + "=" * 60)
print("завдання 6. векторизація f(x)")
print("=" * 60)

def f_scalar(xv):
    """скалярна f(x) з умови."""
    if xv < 5:
        return np.sin(b * xv)
    elif 5 < xv < 7:
        return np.sqrt(abs(b * xv + 5))
    elif xv == 7:
        return np.nan
    else:
        return np.log(xv + b)

big_array = np.linspace(-20, 25, 10000)

# 6a — np.vectorize
f_vec = np.vectorize(f_scalar)
r_vec = f_vec(big_array)
print(f"\n6a) np.vectorize: перші 5 = {np.round(r_vec[:5], 4)}")

# 6b — map
r_map = np.array(list(map(f_scalar, big_array)))
print(f"6b) map():        перші 5 = {np.round(r_map[:5], 4)}")

# 6c — np.where
r_where = np.where(
    big_array < 5, np.sin(b * big_array),
    np.where((big_array > 5) & (big_array < 7),
             np.sqrt(np.abs(b * big_array + 5)),
             np.where(big_array == 7, np.nan, np.log(big_array + b))))
print(f"6c) np.where:     перші 5 = {np.round(r_where[:5], 4)}")

# 6d — порівняння швидкості
print("\n6d) швидкість на 10 000 точках:")

t0 = time.perf_counter()
_ = np.array([f_scalar(v) for v in big_array])
print(f"  for loop:       {(time.perf_counter()-t0)*1000:.2f} мс")

t0 = time.perf_counter()
_ = np.array(list(map(f_scalar, big_array)))
print(f"  map():          {(time.perf_counter()-t0)*1000:.2f} мс")

t0 = time.perf_counter()
_ = f_vec(big_array)
print(f"  np.vectorize(): {(time.perf_counter()-t0)*1000:.2f} мс")

t0 = time.perf_counter()
_ = np.where(big_array < 5, np.sin(b*big_array),
    np.where((big_array>5)&(big_array<7), np.sqrt(np.abs(b*big_array+5)),
    np.where(big_array==7, np.nan, np.log(big_array+b))))
print(f"  np.where():     {(time.perf_counter()-t0)*1000:.2f} мс  ← найшвидший")

print("\nвисновок: np.where повністю векторизований → найшвидший.")
print("for/map/vectorize — Python-рівень ітерацій → повільніші.")