import sys, io, math
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# ============================================================
# варіант 9: a=5, b=91.120, c=226
# ============================================================
a, b, c = 5, 91.120, 226

print("=" * 55)
print("завдання 1. обчислення виразів")
print("=" * 55)

# 1a
print("\n1a)")
print(f"  a + b       = {round(a + b, 2)}")
print(f"  a * b       = {round(a * b, 2)}")
print(f"  c % a       = {round(c % a, 2)}")
# a у ступені (ціла частина від c // a)
power = c // a
print(f"  c // a      = {int(power)}")
print(f"  a ^ (c//a)  = {round(a ** power, 2)}")

# 1b
print("\n1b)")
print(f"  ln(b)       = {round(math.log(b), 2)}")
print(f"  cos(a)      = {round(math.cos(a), 2)}")
# arccos приймає значення з [-1, 1]; c % a може виходити за межі — беремо % 1
val_arccos = (c % a) % 1 if (c % a) > 1 else c % a
print(f"  |arccos(c%a)| = {round(abs(math.acos(val_arccos)), 2)}")
print(f"  exp(a)      = {round(math.exp(a), 2)}")

# 1c -- сума та добуток цифр числа ac 
print("\n1c)")
# формуємо число ac = конкатенація рядків a та c
num_ac = int(str(int(a)) + str(int(c)))
print(f"  число ac    = {num_ac}")
digits = [int(d) for d in str(num_ac)]
print(f"  цифри       = {digits}")

digit_sum = sum(digits)
# добуток без нулів
digit_product = 1
for d in digits:
    if d != 0:
        digit_product *= d

print(f"  сума цифр   = {digit_sum}")
print(f"  добуток цифр (без 0) = {digit_product}")

print("\n" + "=" * 55)
print("завдання 2. рядок str_1")
print("=" * 55)

str_1 = "Your time is limited, so don't waste it living someone else's life"
print(f"  str_1 = '{str_1}'")

# 2a довжина
print(f"\n2a) довжина: {len(str_1)}")

# 2b перше та останнє входження 'w'
first_w = str_1.find('w')
last_w  = str_1.rfind('w')
print(f"2b) перший індекс 'w': {first_w}, останній: {last_w}")

# 2c прописні → заголовні (upper)
print(f"2c) верхній регістр:\n    {str_1.upper()}")

# 2d пробіл → *
print(f"2d) пробіли замінено:\n    {str_1.replace(' ', '*')}")

print("\n" + "=" * 55)
print("завдання 3. операції з рядком str_1")
print("=" * 55)

# 3a розбити на слова (розподільник — пробіл або кома)
import re
words = re.split(r'[ ,]+', str_1)
# прибираємо порожні елементи
words = [w for w in words if w]
print(f"3a) слова: {words}")

# 3b кількість входжень str_2 = "it"
str_2 = "it"
count_it = str_1.count(str_2)
print(f"\n3b) входжень '{str_2}': {count_it}")

# 3c поміняти місцями 2-ге та останнє слово
w = words.copy()
w[1], w[-1] = w[-1], w[1]
print(f"\n3c) після заміни 2-го та останнього:\n    {w}")

# 3d найдовше слово
longest = max(words, key=len)
print(f"\n3d) найдовше слово: '{longest}', літер: {len(longest)}")

# ============================================================
print("\n" + "=" * 55)
print("завдання 4. рядок str_3")
print("=" * 55)

str_3 = "Cisco 3850 | @ London, Green Str | 10.255.1.5 | 255 @"
print(f"  str_3 = '{str_3}'")

# 4a останні 4 елементи (символи)
print(f"\n4a) останні 4 символи: '{str_3[-4:]}'")

# 4b замінити @ на &
print(f"4b) @ → &: '{str_3.replace('@', '&')}'")

# 4c список чисел (цілих та дробових) у рядку
nums_found = re.findall(r'\b\d+(?:\.\d+)?\b', str_3)
nums_list = [float(n) if '.' in n else int(n) for n in nums_found]
print(f"4c) числа у рядку: {nums_list}")

# 4d сума рядків str_1 та str_3
print(f"4d) str_1 + str_3:\n    '{str_1 + str_3}'")

# ============================================================
print("\n" + "=" * 55)
print("завдання 5. список lst_1")
print("=" * 55)

lst_1 = [0, 5, 3, 9, 3, 5, 6, 1, 6, 1, 0, 4, 5, 3, 2, 6, 1, 7, 3, 7, 3]
print(f"  lst_1 = {lst_1}")

# 5a додати новий елемент типу int на індекс 2
lst_1_a = lst_1.copy()
lst_1_a.insert(2, 99)
print(f"\n5a) вставлено 99 на індекс 2:\n    {lst_1_a}")

# 5b відсортувати за зростанням
lst_1_b = sorted(lst_1)
print(f"\n5b) відсортовано:\n    {lst_1_b}")

# 5c зсув по колу праворуч — lst[n] → lst[1], lst[i] → lst[i+1]
lst_1_c = lst_1.copy()
lst_1_c = [lst_1_c[-1]] + lst_1_c[:-1]
print(f"\n5c) зсув праворуч:\n    {lst_1_c}")

# 5d індекс першого входження 5
print(f"\n5d) перший індекс елемента 5: {lst_1.index(5)}")

# ============================================================
print("\n" + "=" * 55)
print("завдання 6. списки lst_1 та lst_2")
print("=" * 55)

lst_2 = [7, 21, 3, 0, 1, 42, 4, 9, 12, -54]
print(f"  lst_1 = {lst_1}")
print(f"  lst_2 = {lst_2}")

# 6a елементи з 8-го по передостанній lst_1 (індекс 7 до -2)
print(f"\n6a) lst_1[7:-1]: {lst_1[7:-1]}")

# 6b індекси та значення max та min lst_2
max_val = max(lst_2)
min_val = min(lst_2)
print(f"\n6b) max={max_val} на індексі {lst_2.index(max_val)}")
print(f"    min={min_val} на індексі {lst_2.index(min_val)}")

# 6c lst_2_5 — елементи |x| > 5
lst_2_5 = [x for x in lst_2 if abs(x) > 5]
print(f"\n6c) |x| > 5: {lst_2_5}")

# 6d спільні елементи lst_1 та lst_2 без дублікатів
lst_new = list(set(lst_1) & set(lst_2))
print(f"\n6d) спільні елементи (без дублікатів): {sorted(lst_new)}")