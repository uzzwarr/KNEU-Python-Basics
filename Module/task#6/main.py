import sys, io
import numpy as np
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# ============================================================
# завдання 6. пошук у відсортованій матриці
# ============================================================

matrix = [
    [15, 20, 40, 85],
    [20, 35, 80, 95],
    [30, 55, 95, 105],
    [40, 80, 100, 120],
]


def staircase_search(M, target):
    # сходинковий пошук від правого верхнього кута, без повного перебору
    rows, cols = len(M), len(M[0])
    r, c = 0, cols - 1
    found = []
    while r < rows and c >= 0:
        v = M[r][c]
        if v == target:
            found.append((r, c))  # знайдено збіг (може бути кілька)
            c -= 1                # рухаємось ліворуч шукати ще
        elif v > target:
            c -= 1                # значення завелике — крок ліворуч
        else:
            r += 1                # значення замале — крок униз
    return found


def search_or_closest(M, target):
    # повертаємо точні збіги, або індекси найближчих елементів
    exact = staircase_search(M, target)
    if exact:
        return exact, target
    best_diff = None
    closest = []
    # уздовж сходинкового шляху шукаємо мінімальне відхилення
    rows, cols = len(M), len(M[0])
    r, c = 0, cols - 1
    while r < rows and c >= 0:
        v = M[r][c]
        diff = abs(v - target)
        if best_diff is None or diff < best_diff:
            best_diff, closest, near_val = diff, [(r, c)], v
        elif diff == best_diff:
            closest.append((r, c))
        c -= 1 if v > target else 0
        r += 1 if v < target else 0
        if v == target:
            break
    return closest, near_val


print("=" * 55)
print("завдання 6. пошук у відсортованій матриці")
print("=" * 55)

print("\nматриця:")
for row in matrix:
    print("  ", row)

# класичний пошук наявного елемента (кілька збігів)
print("\nпошук 55  ->", staircase_search(matrix, 55))
print("пошук 20  ->", staircase_search(matrix, 20), "(два входження)")
print("пошук 95  ->", staircase_search(matrix, 95), "(два входження)")

# елемента немає — повертаємо найближчий
idx, val = search_or_closest(matrix, 83)
print(f"\nпошук 83  -> немає; найближчий {val} за індексом {idx}")

# ------------------- варіант з NumPy -------------------
print("\n--- NumPy ---")
M = np.array(matrix)

# усі індекси точного збігу
print("пошук 95 (NumPy)  ->", np.argwhere(M == 95).tolist())

# найближчий елемент через матрицю абсолютних відхилень
diff = np.abs(M - 83)
nearest = np.argwhere(diff == diff.min())
print("пошук 83 (NumPy)  -> найближчий", M[tuple(nearest[0])],
      "за індексами", nearest.tolist())