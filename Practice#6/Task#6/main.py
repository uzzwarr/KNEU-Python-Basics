"""
Виконати завдання 4-5 ПР № 4 із використанням циклів та умовних
операторів (не використовувати спискові включення, функції map(), filter())

4. для списку list_3 виконати дії із використанням спискових включень та/або map():
   - сформувати list_4 тільки з чисел list_3
   - вивести всі додатні елементи list_4 через спискові включення
   - вивести всі додатні елементи list_4 через map(), filter()
   - створити список квадратів елементів list_4
   - вивести елементи list_3, що є літерами, у верхньому регістрі через спискові включення
   - вивести елементи list_3, що є літерами, у верхньому регістрі через map(), filter()

5. сформувати list_5 із 12 елементів: 8 цілих чисел та 4 рядки.
   на основі list_5 створити list_6 з 8 елементів, де кожен елемент —
   середньоарифметичне всіх наступних числових елементів list_5 (з точністю до 2 знаків).
   наприклад: list_5 = [1, 1, "ASbvsxT", 2, 4, "A", -1, "qq", 7, 2, 0, "qweT"]
   list_6 = [2.00, 2.14, 2.33, 2.40, 2.00, 3.00, 1.00, 0.00]
   також вивести рядки з list_5 з довжиною більше 2.
"""

# ============================================================
# частина 1: list_3 та list_4
# ============================================================

list_3 = [1, "hello", -3, "world", 5.5, 0, "Python", -7, 2, "abc", 8, "!", True]

print("=" * 50)
print(f"list_3: {list_3}")

# --- формування list_4 тільки з чисел (bool виключаємо, бо bool є підкласом int) ---
list_4 = [x for x in list_3 if isinstance(x, (int, float)) and not isinstance(x, bool)]
print(f"\nlist_4 (тільки числа): {list_4}")

# --- додатні елементи list_4 через спискове включення ---
positive_comp = [x for x in list_4 if x > 0]
print(f"\nдодатні елементи (спискове включення): {positive_comp}")

# --- додатні елементи list_4 через filter() ---
positive_filter = list(filter(lambda x: x > 0, list_4))
print(f"додатні елементи (filter):              {positive_filter}")

# map() тут не дає переваги для фільтрації, тому поєднуємо з filter
positive_map_filter = list(map(lambda x: x, filter(lambda x: x > 0, list_4)))
print(f"додатні елементи (map + filter):        {positive_map_filter}")

# --- квадрати елементів list_4 ---
squares = [x ** 2 for x in list_4]
print(f"\nквадрати list_4 (спискове включення): {squares}")

squares_map = list(map(lambda x: x ** 2, list_4))
print(f"квадрати list_4 (map):                {squares_map}")

# --- літери list_3 у верхньому регістрі через спискове включення ---
# рядки, що складаються тільки з літер (str та isalpha)
upper_comp = [x.upper() for x in list_3 if isinstance(x, str) and x.isalpha()]
print(f"\nлітери у верхньому регістрі (спискове включення): {upper_comp}")

# --- літери list_3 у верхньому регістрі через map() та filter() ---
only_alpha = list(filter(lambda x: isinstance(x, str) and x.isalpha(), list_3))
upper_map = list(map(lambda x: x.upper(), only_alpha))
print(f"літери у верхньому регістрі (map + filter):        {upper_map}")

# ============================================================
# частина 2: list_5 та list_6
# ============================================================

print("\n" + "=" * 50)

list_5 = [1, 1, "ASbvsxT", 2, 4, "A", -1, "qq", 7, 2, 0, "qweT"]
print(f"list_5: {list_5}")

# витягуємо лише числові елементи зі збереженням позицій (індексів)
# num_indices[i] = індекс i-го числа в list_5
num_indices = []
for idx, val in enumerate(list_5):
    if isinstance(val, (int, float)) and not isinstance(val, bool):
        num_indices.append(idx)

# формування list_6: для кожного числового елемента —
# середнє арифметичне всіх НАСТУПНИХ числових елементів
list_6 = []
num_count = len(num_indices)

for i in range(num_count):
    # наступні числові елементи починаючи з поточного включно
    # (за прикладом: перший елемент = середнє всіх числових)
    following_nums = [list_5[num_indices[j]] for j in range(i, num_count)]

    if len(following_nums) == 0:
        avg = 0.0
    else:
        avg = sum(following_nums) / len(following_nums)

    list_6.append(round(avg, 2))

print(f"list_6: {list_6}")

# --- рядки з list_5 з довжиною більше 2 ---
# використовуємо цикл без спискових включень (умова завдання для цієї частини)
print("\nрядки з list_5 з довжиною більше 2:")
for item in list_5:
    if isinstance(item, str) and len(item) > 2:
        print(f"  '{item}'")