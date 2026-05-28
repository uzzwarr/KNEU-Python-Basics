import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# ============================================================
# завдання 2. об'єднання двох словників
# ============================================================


def merge_dicts(d1, d2):
    # просте об'єднання: значення d2 перезаписують d1
    return {**d1, **d2}


def merge_sorted(d1, d2):
    # об'єднуємо та сортуємо пари за ключами в алфавітному порядку
    merged = {**d1, **d2}
    return dict(sorted(merged.items()))


def merge_keep_first(d1, d2):
    # при дублюванні ключів зберігаємо значення з першого словника
    result = dict(d2)
    result.update(d1)
    return dict(sorted(result.items()))


def merge_checked(d1, d2):
    # ключі обох словників мають бути рядками
    for d in (d1, d2):
        if not all(isinstance(k, str) for k in d):
            return "помилка: усі ключі мають бути рядками"
    return merge_sorted(d1, d2)


print("=" * 55)
print("завдання 2. словники")
print("=" * 55)

a = {"banana": 3, "apple": 1, "cherry": 5}
b = {"date": 4, "apple": 9, "fig": 2}

# 2а — звичайне об'єднання
print("\n2a) об'єднання:")
print(f"  {merge_dicts(a, b)}")

# 2б — об'єднання з сортуванням за ключами
print("\n2b) з сортуванням за ключами:")
print(f"  {merge_sorted(a, b)}")

# 2в — дублікати: пріоритет першого словника
print("\n2c) дублікати (значення з першого):")
print(f"  {merge_keep_first(a, b)}")        # apple=1, не 9

# 2г — перевірка типів ключів
print("\n2d) перевірка типів ключів:")
print(f"  рядкові ключі: {merge_checked(a, b)}")
print(f"  числові ключі: {merge_checked({1: 'x'}, {2: 'y'})}")