"""
бонусне завдання:
задано відсортовану матрицю розміру MxN цілих чисел (рядки та стовпці відсортовані).
запропонувати алгоритм пошуку довільного елемента.

реалізація:
 1. пошук без повного перебору (алгоритм з правого верхнього кута) — O(M+N);
 2. пошук для випадку, коли таких елементів кілька;
 3. пошук методом бінарного пошуку по кожному рядку — O(M * log N);
 4. пошук найближчого елемента, якщо шуканого нема;
 5. всі варіанти з використанням бібліотеки NumPy.

приклад матриці:
 15  20  40  85
 20  35  80  95
 30  55  95 105
 40  80 100 120
"""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

import numpy as np

# матриця з умови задачі
MATRIX = [
    [ 15,  20,  40,  85],
    [ 20,  35,  80,  95],
    [ 30,  55,  95, 105],
    [ 40,  80, 100, 120],
]

# ============================================================
# спосіб 1: пошук без повного перебору — алгоритм з правого верхнього кута
# складність O(M + N): починаємо з правого верхнього кута,
# йдемо вліво якщо поточний > target, вниз якщо < target
# ============================================================
def search_no_full_scan(matrix, target):
    """
    пошук елемента без повного перебору.
    повертає (рядок, стовпець) або None якщо не знайдено.
    алгоритм: стартуємо з правого верхнього кута.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    # стартова позиція — правий верхній кут
    row, col = 0, cols - 1
    steps = 0

    while row < rows and col >= 0:
        steps += 1
        current = matrix[row][col]

        if current == target:
            print(f"  знайдено за {steps} кроків")
            return (row, col)
        elif current > target:
            # поточний більший — йдемо вліво
            col -= 1
        else:
            # поточний менший — йдемо вниз
            row += 1

    print(f"  не знайдено за {steps} кроків")
    return None


# ============================================================
# спосіб 2: пошук всіх входжень (коли елементів кілька)
# використовує той самий алгоритм, але продовжує після знахідки
# ============================================================
def search_all_occurrences(matrix, target):
    """
    знаходить всі позиції елемента в матриці без повного перебору.
    після знаходження елемента продовжує пошук у залишкових зонах.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    results = []

    visited = set()

    def _scan(row_start, row_end, col_start, col_end):
        """рекурсивний пошук у підматриці."""
        if row_start > row_end or col_start > col_end:
            return

        row, col = row_start, col_end

        while row <= row_end and col >= col_start:
            current = matrix[row][col]
            if current == target:
                # додаємо лише якщо не було знайдено раніше
                if (row, col) not in visited:
                    visited.add((row, col))
                    results.append((row, col))
                # шукаємо далі: вниз і вліво окремо
                _scan(row + 1, row_end, col_start, col)
                _scan(row, row_end, col_start, col - 1)
                return
            elif current > target:
                col -= 1
            else:
                row += 1

    _scan(0, rows - 1, 0, cols - 1)
    return results


# ============================================================
# спосіб 3: бінарний пошук по кожному рядку — O(M * log N)
# ============================================================
def binary_search_row(arr, target):
    """бінарний пошук у відсортованому масиві, повертає індекс або -1."""
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def search_binary(matrix, target):
    """
    бінарний пошук по кожному рядку матриці.
    повертає список (рядок, стовпець) для всіх знахідок.
    """
    results = []
    for r, row in enumerate(matrix):
        col = binary_search_row(row, target)
        if col != -1:
            results.append((r, col))
    return results


# ============================================================
# спосіб 4: пошук найближчого елемента якщо target не знайдено
# ============================================================
def search_closest(matrix, target):
    """
    шукає target; якщо не знайдено — повертає позиції елементів
    з мінімальним відхиленням від target.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    # спочатку спробуємо знайти точне значення
    exact = search_all_occurrences(matrix, target)
    if exact:
        return exact, 0   # знайдено точно, відхилення 0

    # шукаємо мінімальне відхилення по всій матриці
    min_diff = float("inf")
    closest = []

    for r in range(rows):
        for c in range(cols):
            diff = abs(matrix[r][c] - target)
            if diff < min_diff:
                min_diff = diff
                closest = [(r, c)]
            elif diff == min_diff:
                closest.append((r, c))

    return closest, min_diff


# ============================================================
# спосіб 5: всі варіанти з NumPy
# ============================================================
def numpy_search_no_full_scan(np_matrix, target):
    """алгоритм правого верхнього кута через numpy."""
    rows, cols = np_matrix.shape
    row, col = 0, cols - 1
    steps = 0

    while row < rows and col >= 0:
        steps += 1
        val = np_matrix[row, col]
        if val == target:
            print(f"  numpy: знайдено за {steps} кроків")
            return (row, col)
        elif val > target:
            col -= 1
        else:
            row += 1

    print(f"  numpy: не знайдено за {steps} кроків")
    return None


def numpy_search_all(np_matrix, target):
    """
    numpy пошук всіх входжень через np.where.
    повертає список кортежів (рядок, стовпець).
    """
    rows, cols = np.where(np_matrix == target)
    return list(zip(rows.tolist(), cols.tolist()))


def numpy_binary_search(np_matrix, target):
    """бінарний пошук по кожному рядку через np.searchsorted."""
    results = []
    for r in range(np_matrix.shape[0]):
        row = np_matrix[r]
        # searchsorted повертає позицію вставки
        idx = np.searchsorted(row, target)
        if idx < len(row) and row[idx] == target:
            results.append((r, int(idx)))
    return results


def numpy_search_closest(np_matrix, target):
    """
    numpy пошук найближчого елемента.
    повертає позиції та мінімальне відхилення.
    """
    # перевіряємо точне входження
    exact = numpy_search_all(np_matrix, target)
    if exact:
        return exact, 0

    # матриця відхилень
    diff_matrix = np.abs(np_matrix - target)
    min_diff = diff_matrix.min()
    rows, cols = np.where(diff_matrix == min_diff)
    return list(zip(rows.tolist(), cols.tolist())), int(min_diff)

def print_matrix(matrix):
    """виводить матрицю у форматованому вигляді."""
    for row in matrix:
        print("  " + "  ".join(f"{v:4d}" for v in row))


print("=" * 55)
print("матриця:")
print_matrix(MATRIX)
np_matrix = np.array(MATRIX)

# пошук існуючого елемента без повного перебору ---
target = 55
print(f"\n--- спосіб 1: пошук {target} без повного перебору ---")
result = search_no_full_scan(MATRIX, target)
print(f"  результат: {result} → значення {MATRIX[result[0]][result[1]]}")

# пошук всіх входжень (елемент 20 є двічі) 
target_dup = 20
print(f"\n--- спосіб 2: всі входження {target_dup} ---")
all_res = search_all_occurrences(MATRIX, target_dup)
print(f"  знайдено на позиціях: {all_res}")
for r, c in all_res:
    print(f"    [{r}][{c}] = {MATRIX[r][c]}")

# бінарний пошук 
print(f"\n--- спосіб 3: бінарний пошук {target} ---")
bin_res = search_binary(MATRIX, target)
print(f"  знайдено: {bin_res}")

# пошук найближчого (83 не існує → має знайти 85)
target_miss = 83
print(f"\n--- спосіб 4: пошук найближчого до {target_miss} ---")
closest_res, diff = search_closest(MATRIX, target_miss)
print(f"  найближчі позиції: {closest_res}, відхилення: {diff}")
for r, c in closest_res:
    print(f"    [{r}][{c}] = {MATRIX[r][c]}")

print("\n" + "=" * 55)
print("NumPy варіанти:")
print(f"  np_matrix:\n{np_matrix}\n")

# numpy тест 1: без повного перебору
print(f"--- numpy 1: пошук {target} без повного перебору ---")
np_res1 = numpy_search_no_full_scan(np_matrix, target)
print(f"  результат: {np_res1} → значення {np_matrix[np_res1]}")

# numpy тест 2: всі входження
print(f"\n--- numpy 2: всі входження {target_dup} ---")
np_res2 = numpy_search_all(np_matrix, target_dup)
print(f"  знайдено: {np_res2}")
for r, c in np_res2:
    print(f"    [{r}][{c}] = {np_matrix[r, c]}")

# numpy тест 3: бінарний пошук 
print(f"\n--- numpy 3: бінарний пошук {target} ---")
np_res3 = numpy_binary_search(np_matrix, target)
print(f"  знайдено: {np_res3}")

# numpy тест 4: найближчий елемент
print(f"\n--- numpy 4: найближчий до {target_miss} ---")
np_res4, np_diff = numpy_search_closest(np_matrix, target_miss)
print(f"  найближчі позиції: {np_res4}, відхилення: {np_diff}")
for r, c in np_res4:
    print(f"    [{r}][{c}] = {np_matrix[r, c]}")