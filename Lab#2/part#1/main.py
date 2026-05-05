"""
лабораторна робота №2_1. numpy — варіант 9
параметри варіанту:
  x — масив довжини 16, випадкові цілі з [-10, 6) з кроком 2
  y — масив довжини 16, випадкові цілі з (0, 1) (рівномірний розподіл)
  a = 4, n = 4, m = 5
  start = -15, end = 15, step = 1
  seed: np.random.RandomState(96)
"""
 
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
 
import numpy as np
 
# ініціалізація генератора
rng = np.random.RandomState(96)
 
# параметри варіанту
a, n, m = 4, 4, 5
start, end, step = -15, 15, 1
 
# масив x: цілі з [-10, 6) з кроком 2 → можливі значення: -10,-8,-6,-4,-2,0,2,4
pool_x = np.arange(-10, 6, 2)               # [-10,-8,-6,-4,-2, 0, 2, 4]
x = rng.choice(pool_x, size=16)
 
# масив y: рівномірний розподіл (0, 1)
y = rng.uniform(0, 1, size=16)
 
print("=" * 60)
print("вхідні дані:")
print(f"  a={a}, n={n}, m={m}, start={start}, end={end}, step={step}")
print(f"  x = {x}")
print(f"  y = {np.round(y, 4)}")
 
print("\n" + "=" * 60)
print("завдання 1. операції з масивами x, y та числом a")
print("=" * 60)
 
# 1a
print("\n1a)")
print(f"  x + y        = {np.round(x + y, 2)}")
print(f"  x * a        = {x * a}")
# ділення на a — якщо є нулі в x, вони дають 0 % a = 0
print(f"  x % a        = {x % a}")
print(f"  x ^ a        = {x ** a}")
 
# 1b — ln(x) лише для додатних x
print("\n1b)")
x_pos = np.where(x > 0, x, np.nan)         # замінюємо ≤0 на nan
print(f"  ln(x) (x>0) = {np.round(np.log(x_pos), 4)}")
print(f"  cos(y)       = {np.round(np.cos(y), 4)}")
print(f"  |y|          = {np.round(np.abs(y), 4)}")
x_safe = np.where(x != 0, x, np.nan)
print(f"  exp(x)       = {np.round(np.exp(x.astype(float)), 2)}")
 
# 1c — максимум x та його індекс
print("\n1c)")
max_x = np.max(x)
idx_max_x = np.argmax(x)
print(f"  max(x) = {max_x}, індекс = {idx_max_x}")
 
# 1d — розгорнути y
print("\n1d)")
y_rev = y[::-1]
print(f"  y розгорнуто = {np.round(y_rev, 4)}")
 
print("\n" + "=" * 60)
print("завдання 2. зрізи масивів")
print("=" * 60)
 
# 2a — x: парні індекси починаючи з індексу 2
print("\n2a) x[2::2]:", x[2::2])
 
# 2b — y: кожен 3-й починаючи з передостаннього (індекс -2), іде назад
print("2b) y[-2::-3]:", np.round(y[-2::-3], 4))
 
# 2c — x+y: перші 3 та останні 3
xy = x + y
print(f"2c) (x+y)[:3] = {np.round(xy[:3], 4)}")
print(f"    (x+y)[-3:] = {np.round(xy[-3:], 4)}")
 
# 2d — найближчий до a елемент масиву x
print("\n2d)")
idx_closest = np.argmin(np.abs(x - a))
print(f"  найближчий до a={a} у x: x[{idx_closest}] = {x[idx_closest]}")
 
print("\n" + "=" * 60)
print("завдання 3. створення масивів")
print("=" * 60)
 
# 3a — 1D масив від 0 до n*m-1
arr_3a = np.arange(n * m)
print(f"\n3a) arange(n*m={n*m}):\n  {arr_3a}")
 
# 3b — 2D масив n*m, випадкові float з [-m, m]
arr_3b = rng.uniform(-m, m, size=(n, m))
print(f"\n3b) 2D float [{-m}, {m}], форма {n}x{m}:\n{np.round(arr_3b, 4)}")
 
# 3c — 2D масив n*m, випадкові float з (0,1), округлити до 2 знаків
arr_3c = np.round(rng.uniform(0, 1, size=(n, m)), 2)
print(f"\n3c) 2D float (0,1) округл. до 2 знаків, форма {n}x{m}:\n{arr_3c}")
 
# 3d — матриця m*n з одиниць, тип int
arr_3d = np.ones((m, n), dtype=int)
print(f"\n3d) ones ({m}x{n}, int):\n{arr_3d}")
 
# 3e-i — матриця m*m: одиниці на головній діагоналі, тип float
arr_3e_main = np.eye(m, dtype=float)
print(f"\n3e-i) eye({m}x{m}, головна діагональ, float):\n{arr_3e_main}")
 
# 3e-ii — матриця m*m: одиниці на 1-й діагоналі (вище головної, k=1)
arr_3e_1 = np.eye(m, k=1, dtype=float)
print(f"\n3e-ii) eye({m}x{m}, діагональ k=1):\n{arr_3e_1}")
 
# 3f — 3D масив n*m*3, цілі з (-n, n) з кроком 2
pool_3f = np.arange(-n + 1, n, 2)          # непарні з (-n, n) крок 2
arr_3f = rng.choice(pool_3f, size=(n, m, 3))
print(f"\n3f) 3D ({n}x{m}x3), цілі (-{n},{n}) крок 2:\n{arr_3f}")

print("\n" + "=" * 60)
print("завдання 4. зміна форми масиву x")
print("=" * 60)
 
# 4a — вектор-рядок
x_row = x.reshape(1, -1)
print(f"\n4a) вектор-рядок (1x{len(x)}):\n{x_row}")
 
# 4b — вектор-стовпець
x_col = x.reshape(-1, 1)
print(f"\n4b) вектор-стовпець ({len(x)}x1):\n{x_col.T}  (транспоновано для компактності)")
 
# 4c — матриця X 4*4, нулі на головній діагоналі
X = x.reshape(4, 4).copy()
np.fill_diagonal(X, 0)
print(f"\n4c) матриця X (4x4), нулі на діагоналі:\n{X}")
 
# 4d — транспонована X
X_T = X.T
print(f"\n4d) X транспоновано:\n{X_T}")
 
print("\n" + "=" * 60)
print("завдання 5. матриця A (6x6)")
print("=" * 60)
 
# матриця A 6x6, цілі з [start, end] з кроком step
pool_A = np.arange(start, end + 1, step)
A = rng.choice(pool_A, size=(6, 6))
print(f"\nматриця A (6x6):\n{A}")
 
# 5a — min та max
print(f"\n5a) min(A) = {A.min()},  max(A) = {A.max()}")
 
# 5b — індекси min та max (unravel для 2D)
print(f"5b) індекс min: {np.unravel_index(A.argmin(), A.shape)}")
print(f"    індекс max: {np.unravel_index(A.argmax(), A.shape)}")
 
# 5c — поміняти 1-й та 3-й рядки (індекси 0 та 2)
A_swapped = A.copy()
A_swapped[[0, 2]] = A_swapped[[2, 0]]
print(f"\n5c) A після перестановки рядків 0 та 2:\n{A_swapped}")
 
# 5d — середнє по стовпцях та рядках
print(f"\n5d) середнє по стовпцях: {np.round(A.mean(axis=0), 2)}")
print(f"    середнє по рядках:   {np.round(A.mean(axis=1), 2)}")

print("\n" + "=" * 60)
print("завдання 6. операції з матрицею A")
print("=" * 60)
 
# 6a — форма 9*4 (36 елементів → 9*4=36 ✓)
A_flat = A.reshape(9, 4)
print(f"\n6a) A форма (9x4):\n{A_flat}")
 
# 6b — розбити (9x4) по вертикалі: верх (5x4) та низ (4x4)
A_up     = A_flat[:5, :]
A_bottom = A_flat[5:, :]
print(f"\n6b) A_up (5x4):\n{A_up}")
print(f"    A_bottom (4x4):\n{A_bottom}")
 
# 6c — поєднати по вертикалі A_bottom (4x4) та X (4x4)
AC_vert = np.vstack([A_bottom, X])
print(f"\n6c) vstack(A_bottom, X) — форма {AC_vert.shape}:\n{AC_vert}")
 
# 6d — поєднати по горизонталі A_bottom (4x4) та X (4x4)
AC_horiz = np.hstack([A_bottom, X])
print(f"\n6d) hstack(A_bottom, X) — форма {AC_horiz.shape}:\n{AC_horiz}")
 
# 6e — розбити AC_horiz по горизонталі: ліва (4x7) та права (4x1, останній стовпець)
AC_left  = AC_horiz[:, :-1]
AC_right = AC_horiz[:, -1:]
print(f"\n6e) ліва частина (4x{AC_left.shape[1]}):\n{AC_left}")
print(f"    права частина (4x1, останній стовпець):\n{AC_right}")
