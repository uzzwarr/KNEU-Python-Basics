import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# ============================================================
# завдання 3. операції над списками
# ============================================================


def common_unique(x, y):
    # унікальні елементи, що присутні в обох списках
    return sorted(set(x) & set(y))


def remove_duplicates(lst):
    # видаляємо дублікати, зберігаючи початковий порядок
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def average(numbers):
    # середнє через генератор — економимо пам'ять, не будуючи список
    gen = (n for n in numbers)
    total, count = 0, 0
    for n in gen:
        total += n
        count += 1
    return total / count if count else 0


def filter_transform(lst, cond1, cond2):
    # лишаємо елементи, що задовольняють обидва критерії, і підносимо до квадрату
    return [n ** 2 for n in lst if cond1(n) and cond2(n)]


print("=" * 55)
print("завдання 3. списки")
print("=" * 55)

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [4, 5, 6, 9, 10, 4, 5]

# 3а — спільні унікальні елементи
print("\n3a) спільні унікальні елементи:")
print(f"  {common_unique(x, y)}")

# 3б — видалення дублікатів зі збереженням порядку
print("\n3b) без дублікатів (порядок збережено):")
print(f"  {remove_duplicates(y)}")

# 3в — середнє значення через генератор
print("\n3c) середнє значення x:")
print(f"  {average(x)}")

# 3г — фільтрація за двома критеріями + квадрат
print("\n3d) парні та > 2, піднесені до квадрату:")
print(f"  {filter_transform(x, lambda n: n % 2 == 0, lambda n: n > 2)}")