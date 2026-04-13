"""
Згенерувати список цілих випадкових цілих чисел: list_1 з 10 елементів
із діапазону [-3, 6]. З використанням lambda функцій та функцій map(), filter()
вирішити такі завдання:
 написати функцію, яка повертає список чисел з list_1, що є кратними
заданому числу;
 обчислити суму квадратів чисел у списку;
 підрахувати кількість парних чисел у списку;
 знайти суму всіх непарних чисел у списку;
 знайти добуток всіх чисел у списку (окрім нулів);
 видалити всі входження конкретного елемента із списку;
 написати функцію, яка обчислює середнє арифметичне значення
елементів списку, і виводить це значення та всі числа, які більше
середнього значення
"""

import random
from functools import reduce

# генерація списку з введеним seed для відтворюваності
seed = int(input("введіть seed для генератора випадкових чисел (наприклад 42): "))
random.seed(seed)
list_1 = [random.randint(-3, 6) for _ in range(10)]
print(f"\nзгенерований list_1: {list_1}\n")


# числа, кратні заданому
def multiples_of(lst, n):
    return list(filter(lambda x: x % n == 0, lst))


# сума квадратів
def sum_of_squares(lst):
    return sum(map(lambda x: x ** 2, lst))


# кількість парних чисел
def count_even(lst):
    return len(list(filter(lambda x: x % 2 == 0, lst)))


# сума непарних чисел
def sum_odd(lst):
    return sum(filter(lambda x: x % 2 != 0, lst))


# добуток чисел без нулів
def product_no_zeros(lst):
    non_zero = list(filter(lambda x: x != 0, lst))
    if not non_zero:
        return 0
    return reduce(lambda a, b: a * b, non_zero)


# видалення конкретного елемента
def remove_element(lst, elem):
    return list(filter(lambda x: x != elem, lst))


# середнє та числа більші за нього
def above_average(lst):
    """обчислює середнє та виводить числа, що перевищують його."""
    if not lst:
        return
    avg = sum(lst) / len(lst)
    greater = list(filter(lambda x: x > avg, lst))
    print(f"  середнє: {avg:.2f}")
    print(f"  числа більші за середнє: {greater}")



# введення числа для кратності
n = int(input("введіть число для пошуку кратних елементів: "))
print(f"кратні {n}:", multiples_of(list_1, n))

print("сума квадратів:", sum_of_squares(list_1))
print("кількість парних:", count_even(list_1))
print("сума непарних:", sum_odd(list_1))
print("добуток без нулів:", product_no_zeros(list_1))

# введення елемента для видалення
elem = int(input("\nвведіть елемент для видалення зі списку: "))
print(f"список без елемента {elem}:", remove_element(list_1, elem))

print("\nсереднє та числа вище нього:")
above_average(list_1)