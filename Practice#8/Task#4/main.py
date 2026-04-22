"""
завдання 4:
створити одновимірний масив g розмірністю 24, заповнений
випадковими цілими числами з діапазону від -6 до 6.
 - перетворити на вектор-рядок 1*24 та знайти max, min та їх індекси;
 - знайти суму, середнє та індекс елемента, що найменше відхиляється від середнього;
 - перетворити g на матрицю B розмірності 4*6 та знайти max, min та їх індекси;
 - відсортувати матрицю за: а) 2-м стовпцем; б) 1-м рядком;
 - знайти max і min по стовпцях, середнє та суму по рядках.
"""
 
import numpy as np
 
# генерація масиву g
np.random.seed(7)
g = np.random.randint(-6, 7, size=24)
print("масив g:", g)
 
# вектор-рядок 1*24 
row = g.reshape(1, 24)
print("\nвектор-рядок (1x24):", row)
 
# максимум, мінімум та їх індекси у векторі
max_val = row.max()
min_val = row.min()
max_idx = row.argmax()
min_idx = row.argmin()
print(f"max={max_val} (індекс {max_idx}), min={min_val} (індекс {min_idx})")
 
total = g.sum()
mean = g.mean()
# індекс елемента з мінімальним відхиленням від середнього
closest_idx = np.argmin(np.abs(g - mean))
print(f"\nсума: {total}, середнє: {mean:.4f}")
print(f"найближчий до середнього: g[{closest_idx}] = {g[closest_idx]}")
 
# матриця B розмірності 4*6 
B = g.reshape(4, 6)
print("\nматриця B (4x6):\n", B)
 
# max і min матриці та їх індекси (розгорнуті у рядок)
b_max = B.max()
b_min = B.min()
b_max_idx = np.unravel_index(B.argmax(), B.shape)
b_min_idx = np.unravel_index(B.argmin(), B.shape)
print(f"max B={b_max} на позиції {b_max_idx}, min B={b_min} на позиції {b_min_idx}")
 
# argsort повертає індекси рядків у потрібному порядку
sort_by_col = B[B[:, 1].argsort()]
print("\nматриця B відсортована за 2-м стовпцем:\n", sort_by_col)
 
# сортування за 1-м рядком (індекс 0) 
sort_by_row = B[:, B[0].argsort()]
print("\nматриця B відсортована за 1-м рядком:\n", sort_by_row)
 
print("\nmax по стовпцях:", B.max(axis=0))
print("min по стовпцях:", B.min(axis=0))

# середнє та сума по рядках 
print("середнє по рядках:", np.round(B.mean(axis=1), 4))
print("сума по рядках:", B.sum(axis=1))
