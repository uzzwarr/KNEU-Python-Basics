"""
завдання 5:
для матриці B з п.4:
 - з використанням булевих масок та np.any(), np.all(), np.where()
   перевірити: а) чи є елементи > 5; б) чи всі елементи > -5;
 - відібрати парні елементи, що більше 0;
 - замінити всі значення 0 на 10;
 - розбити матрицю B на дві матриці 2*6 по вертикалі;
 - розбити матрицю B на дві матриці 4*3 по горизонталі.
"""
 
import numpy as np
 
# відновлення матриці B 
np.random.seed(7)
g = np.random.randint(-6, 7, size=24)
B = g.reshape(4, 6)
print("матриця B (4x6):\n", B)

# а) чи є елементи більші за 5
has_gt5 = np.any(B > 5)
print(f"\nчи є елементи > 5: {has_gt5}")
# позиції таких елементів через np.where
positions_gt5 = np.where(B > 5)
print("позиції елементів > 5 (рядок, стовпець):", list(zip(*positions_gt5)))
 
# б) чи всі елементи більші за -5
all_gt_neg5 = np.all(B > -5)
print(f"\nчи всі елементи > -5: {all_gt_neg5}")
 
# відбір парних елементів більших за 0 
mask_even_pos = (B % 2 == 0) & (B > 0)
even_positive = B[mask_even_pos]
print("\nпарні елементи > 0:", even_positive)
 
# заміна всіх 0 на 10 
B_no_zero = B.copy()
B_no_zero[B_no_zero == 0] = 10
print("\nматриця B після заміни 0 на 10:\n", B_no_zero)
 
# np.vsplit розбиває по рядках (вертикально)
top, bottom = np.vsplit(B, 2)
print("\nрозбиття по вертикалі (vsplit):")
print("верхня частина (2x6):\n", top)
print("нижня частина (2x6):\n", bottom)
 
# np.hsplit розбиває по стовпцях (горизонтально)
left, right = np.hsplit(B, 2)
print("\nрозбиття по горизонталі (hsplit):")
print("ліва частина (4x3):\n", left)
print("права частина (4x3):\n", right)
