"""
1.	Створіть програму, яка запитує користувача два цілих числа a і b,
після чого виводить на екран результати наступних математичних операцій
(результат округлити до 2-х знаків після коми):
"""

import math

a = int(input("Введіть значення числа a: "))
b = int(input("Введіть значення числа b: "))

print(round(a + b, 2))
print(round(a - b, 2))
print(round(a * b, 2))
print(round(a / b, 2))
print(round(a % b, 2))
print(round(a ** b, 2))

print(round(math.log10(a), 2))

print(round(math.sqrt(a), 2))

a, b = b, a
print("Нові значення чисел a та b : ", a, b)