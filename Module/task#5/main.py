import sys, io
import numpy as np
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# ============================================================
# завдання 5. матричні операції з NumPy
# ============================================================

np.random.seed(9)  # фіксуємо seed для відтворюваності результату

# створюємо два масиви по 16 цілих чисел з діапазону [-10, 10]
arr_a = np.random.randint(-10, 11, 16)
arr_b = np.random.randint(-10, 11, 16)

print("=" * 55)
print("завдання 5. NumPy матриці")
print("=" * 55)

# формуємо з масивів дві матриці 4x4
A = arr_a.reshape(4, 4)
B = arr_b.reshape(4, 4)
print("\nматриця A:\n", A)
print("\nматриця B:\n", B)

# знаходимо індекси всіх від'ємних елементів матриці A
neg_idx = np.argwhere(A < 0)
print("\nіндекси від'ємних елементів A:")
print(neg_idx.tolist())

# поелементна сума, добуток та транспонована від добутку
print("\nпоелементна сума A + B:\n", A + B)
prod = A * B
print("\nпоелементний добуток A * B:\n", prod)
print("\nтранспонований добуток (A*B).T:\n", prod.T)

# змінюємо форму матриці B
print("\nB reshape (2, 8):\n", B.reshape(2, 8))
print("\nB reshape (16, 1):\n", B.reshape(16, 1).ravel(), "(як стовпець)")
print("\nB reshape (16,):\n", B.reshape(16))

# розбиваємо A по вертикалі на дві матриці 2x4
top, bottom = np.vsplit(A, 2)
print("\nрозбиття A по вертикалі (2x4):")
print(top, "\n", bottom)

# розбиваємо A по горизонталі на дві матриці 4x2
left, right = np.hsplit(A, 2)
print("\nрозбиття A по горизонталі (4x2):")
print(left, "\n", right)