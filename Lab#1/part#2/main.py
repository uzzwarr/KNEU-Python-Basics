import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

lst_1 = [0, 5, 3, 9, 3, 5, 6, 1, 6, 1, 0, 4, 5, 3, 2, 6, 1, 7, 3, 7, 3]
lst_2 = [7, 21, 3, 0, 1, 42, 4, 9, 12, -54]
lst_3 = [22, 19, 16, 13, 10, 7, 4, 1]

# ============================================================
print("=" * 55)
print("завдання 1. словник")
print("=" * 55)

d = {"alpha": 1, "beta": 2, "gamma": 3, "delta": 4, "epsilon": 5}
print(f"  словник: {d}")

# 1a - поміняти місцями перший та останній елементи
keys = list(d.keys())
vals = list(d.values())
vals[0], vals[-1] = vals[-1], vals[0]
d = dict(zip(keys, vals))
print(f"\n1a) перший↔останній: {d}")

# 1b - видалити другий елемент
keys2 = list(d.keys())
d.pop(keys2[1])
print(f"1b) видалено 2-й: {d}")

# 1c - додати new_key → new_value
d["new_key"] = "new_value"
print(f"1c) додано new_key: {d}")

# 1d - ключі та значення в окремих списках
print(f"1d) ключі:    {list(d.keys())}")
print(f"    значення: {list(d.values())}")

# ============================================================
print("\n" + "=" * 55)
print("завдання 2. словник із підрахунком lst_1")
print("=" * 55)

print(f"  lst_1 = {lst_1}")

# 2a - скільки разів зустрічається кожне число
from collections import Counter
counter = Counter(lst_1)
print(f"\n2a) кількість входжень:\n    {dict(counter)}")

# 2b -словник {унікальний елемент: кількість}
freq_dict = dict(counter)
print(f"\n2b) словник частот: {freq_dict}")

# 2c - відсортований за зростанням ключів
sorted_dict = dict(sorted(freq_dict.items()))
print(f"\n2c) відсортовано за ключами: {sorted_dict}")

# 2d - три ключі з найбільшими значеннями
top3 = sorted(freq_dict, key=lambda k: freq_dict[k], reverse=True)[:3]
print(f"\n2d) топ-3 ключі за частотою: {top3} → {[freq_dict[k] for k in top3]} входжень")

# ============================================================
print("\n" + "=" * 55)
print("завдання 3. lst_3 та lambda-функції")
print("=" * 55)

print(f"  lst_3 = {lst_3}")

# 3a - квадрати елементів 
print("\n3a) квадрати:")
# і) цикл
sq_loop = []
for x in lst_3:
    sq_loop.append(x ** 2)
print(f"  цикл:     {sq_loop}")
# іі) map
sq_map = list(map(lambda x: x ** 2, lst_3))
print(f"  map:      {sq_map}")
# ііі) спискове включення
sq_comp = [x ** 2 for x in lst_3]
print(f"  включення:{sq_comp}")

# 3b - парні елементи 
print("\n3b) парні елементи:")
ev_loop = []
for x in lst_3:
    if x % 2 == 0:
        ev_loop.append(x)
print(f"  цикл:     {ev_loop}")
ev_filter = list(filter(lambda x: x % 2 == 0, lst_3))
print(f"  filter:   {ev_filter}")
ev_comp = [x for x in lst_3 if x % 2 == 0]
print(f"  включення:{ev_comp}")

# 3c - залишки від ділення на 3
print("\n3c) залишки від ділення на 3:")
rem_loop = []
for x in lst_3:
    rem_loop.append(x % 3)
print(f"  цикл:     {rem_loop}")
rem_map = list(map(lambda x: x % 3, lst_3))
print(f"  map:      {rem_map}")
rem_comp = [x % 3 for x in lst_3]
print(f"  включення:{rem_comp}")

# 3d - кортеж з елементів та їх індексів
print("\n3d) кортеж (елемент, індекс):")
tup_loop = []
for i, x in enumerate(lst_3):
    tup_loop.append((x, i))
tup_loop = tuple(tup_loop)
print(f"  цикл:     {tup_loop}")
tup_zip = tuple(zip(lst_3, range(len(lst_3))))
print(f"  zip:      {tup_zip}")
tup_comp = tuple((x, i) for i, x in enumerate(lst_3))
print(f"  включення:{tup_comp}")

# ============================================================
print("\n" + "=" * 55)
print("завдання 4. ділення на 6")
print("=" * 55)

def is_divisible_by_6(number):
    """перевіряє чи ділиться число на 6 за двома умовами."""
    n = abs(number)           # враховуємо від'ємні числа
    last_digit = n % 10
    digit_sum  = sum(int(d) for d in str(n))
    if last_digit % 2 == 0 and digit_sum % 3 == 0:
        return f"Число {number} ділиться на 6"
    return f"Число {number} неподільне на 6"

print(f"  lst_2 = {lst_2}")
results = list(map(is_divisible_by_6, lst_2))
for r in results:
    print(f"  {r}")

# ============================================================
print("\n" + "=" * 55)
print("завдання 5. FizzBuzz (1–50) + множини")
print("=" * 55)

fizz     = set()   # діляться на 3
buzz     = set()   # діляться на 5
fizzbuzz = set()   # діляться на 3 і 5
others   = set()   # решта

for n in range(1, 51):
    if n % 3 == 0 and n % 5 == 0:
        fizzbuzz.add(n)
    elif n % 3 == 0:
        fizz.add(n)
    elif n % 5 == 0:
        buzz.add(n)
    else:
        others.add(n)

print(f"5a) Fizz    ({len(fizz)} шт.): {sorted(fizz)}")
print(f"    Buzz    ({len(buzz)} шт.): {sorted(buzz)}")
print(f"    FizzBuzz({len(fizzbuzz)} шт.): {sorted(fizzbuzz)}")
print(f"    Others  ({len(others)} шт.): {sorted(others)}")

# 5b - є у Fizz, але немає у Buzz
fizz_not_buzz = fizz - buzz
print(f"\n5b) Fizz без Buzz: {sorted(fizz_not_buzz)}")

# 5c - перетин Fizz та Buzz
intersection = list(fizz & buzz)
print(f"5c) перетин Fizz ∩ Buzz: {sorted(intersection)}")

# 5d: об'єднання Fizz та Buzz
union = list(fizz | buzz)
print(f"5d) об'єднання Fizz ∪ Buzz: {sorted(union)}")

# ============================================================
print("\n" + "=" * 55)
print("завдання 6. перевірка пароля")
print("=" * 55)

import string

def check_password(password):
    """перевіряє надійність пароля та повертає список помилок."""
    ERR = {
        "length":    "довжина менше 6 символів",
        "uppercase": "немає символів верхнього регістру",
        "lowercase": "немає символів нижнього регістру",
        "digits":    "немає цифр",
        "special":   "немає спеціальних символів",
    }
    errors = {}

    if len(password) < 6:
        errors["length"] = ERR["length"]
    if not any(c.isupper() for c in password):
        errors["uppercase"] = ERR["uppercase"]
    if not any(c.islower() for c in password):
        errors["lowercase"] = ERR["lowercase"]
    if not any(c.isdigit() for c in password):
        errors["digits"] = ERR["digits"]
    if all(c.isalpha() or c.isdigit() for c in password):
        errors["special"] = ERR["special"]

    if not errors:
        return "Пароль припустимий"
    return "Помилки:\n" + "\n".join(f"  - {v}" for v in errors.values())

# тестові паролі
test_passwords = ["abc", "Password1!", "qwerty", "Str0ng@Pass", "12345"]
for pwd in test_passwords:
    print(f"\n  пароль: '{pwd}'")
    print(f"  {check_password(pwd)}")