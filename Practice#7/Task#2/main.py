"""
Напишіть функцію, яка приймає
 словник і друкує його ключі та значення;
 словник та повертає список ключів, впорядкованих за їхніми
значеннями в порядку зростання;
 змінну кількість позиційних числових аргументів і повертає їх суму;
 список чисел і повертає їх суму. Функція повинна мати змінну
кількість іменованих аргументів;
 список чисел і повертає їх середнє значення. Функція повинна мати
змінну кількість позиційних аргументів.
"""

# друк ключів та значень словника
def print_dict(d):
    """друкує кожен ключ та відповідне значення словника."""
    for key, value in d.items():
        print(f"  {key}: {value}")


# ключі, впорядковані за значеннями зростання
def keys_sorted_by_value(d):
    """повертає список ключів словника, відсортованих за їх значеннями."""
    return sorted(d, key=lambda k: d[k])


# сума змінної кількості позиційних аргументів
def sum_args(*args):
    """повертає суму довільної кількості числових позиційних аргументів."""
    total = 0
    for n in args:
        total += n
    return total


# сума списку чисел через змінні іменовані аргументи
def sum_kwargs(**kwargs):
    """повертає суму чисел, переданих як іменовані аргументи."""
    total = 0
    for value in kwargs.values():
        total += value
    return total


# середнє значення через змінну кількість позиційних аргументів
def mean_args(*args):
    """повертає середнє арифметичне довільної кількості позиційних аргументів."""
    if not args:
        return 0
    return sum(args) / len(args)



# введення словника: пари ключ значення через пробіл (apple 3 banana 1 cherry 2)
print("введіть пари ключ значення для словника (наприклад: apple 3 banana 1 cherry 2):")
raw_dict = input(">> ").split()
# перетворення плоского списку у словник {ключ: ціле число}
sample_dict = {raw_dict[i]: int(raw_dict[i + 1]) for i in range(0, len(raw_dict), 2)}

print("\nдрук словника:")
print_dict(sample_dict)
print("ключі за зростанням значень:", keys_sorted_by_value(sample_dict))


raw_args = input("\nвведіть числа через пробіл для суми (*args): ").split()
nums_args = [float(x) for x in raw_args]
print("сума *args:", sum_args(*nums_args))


print("введіть іменовані аргументи для суми (**kwargs) у форматі: a=10 b=20 c=5")
raw_kwargs = input(">> ").split()
# розбиття кожного токену на ім'я та значення
kwargs = {pair.split("=")[0]: float(pair.split("=")[1]) for pair in raw_kwargs}
print("сума **kwargs:", sum_kwargs(**kwargs))

raw_mean = input("\nвведіть числа через пробіл для середнього (*args): ").split()
nums_mean = [float(x) for x in raw_mean]
print("середнє *args:", mean_args(*nums_mean))