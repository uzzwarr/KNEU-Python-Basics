"""
Є п'ять цифр: 1, 2, 3, 4, 5.
За допомогою перестановок із них склали всі можливі комбінації
п'ятизначних чисел (в числах не має бути двох однакових цифр).
Знайдіть кількість цих комбінацій та суму цих чисел.
Скласти програму:
 Із використанням циклів
 Із використанням модулю intertools
 З використанням функції факторіалу та спискових включень
 Використанням рекурсивних функцій та методів рядків

"""

DIGITS = [1, 2, 3, 4, 5]

print("=" * 55)


# спосіб 1: вкладені цикли

print("спосіб 1: вкладені цикли")

count_loops = 0
total_loops = 0

for a in DIGITS:
    for b in DIGITS:
        if b == a:
            continue
        for c in DIGITS:
            if c in (a, b):
                continue
            for d in DIGITS:
                if d in (a, b, c):
                    continue
                for e in DIGITS:
                    if e in (a, b, c, d):
                        continue
                    # формування числа з п'яти цифр
                    number = a * 10000 + b * 1000 + c * 100 + d * 10 + e
                    count_loops += 1
                    total_loops += number

print(f"  кількість: {count_loops}")
print(f"  сума:      {total_loops}")


# спосіб 2: модуль itertools

print("\nспосіб 2: itertools.permutations")

import itertools

count_iter = 0
total_iter = 0

for perm in itertools.permutations(DIGITS):
    # перетворення кортежу цифр на число
    number = perm[0] * 10000 + perm[1] * 1000 + perm[2] * 100 + perm[3] * 10 + perm[4]
    count_iter += 1
    total_iter += number

print(f"  кількість: {count_iter}")
print(f"  сума:      {total_iter}")


# спосіб 3: факторіал + спискові включення
print("\nспосіб 3: факторіал + спискові включення")

import math

# кількість перестановок = 5! = 120
count_fact = math.factorial(len(DIGITS))

# всі перестановки через спискові включення (вкладені генератори)
numbers_fact = [
    a * 10000 + b * 1000 + c * 100 + d * 10 + e
    for a in DIGITS
    for b in DIGITS if b != a
    for c in DIGITS if c not in (a, b)
    for d in DIGITS if d not in (a, b, c)
    for e in DIGITS if e not in (a, b, c, d)
]

total_fact = sum(numbers_fact)

print(f"  кількість (5!): {count_fact}")
print(f"  сума:           {total_fact}")


# спосіб 4: рекурсивна функція + методи рядків
print("\nспосіб 4: рекурсія + методи рядків")


def get_permutations(remaining: str, current: str = "") -> list:
    """рекурсивно генерує всі перестановки рядка remaining."""
    # базовий випадок: всі цифри використані
    if not remaining:
        return [current]

    result = []
    for i in range(len(remaining)):
        # обираємо i-ту цифру, решта — залишок
        chosen = remaining[i]
        rest = remaining[:i] + remaining[i + 1:]
        # рекурсивний виклик з оновленим рядком
        result += get_permutations(rest, current + chosen)
    return result


# рядок із цифр для зручного зрізу методами рядків
digits_str = "".join(str(d) for d in DIGITS)
all_perms = get_permutations(digits_str)

count_rec = len(all_perms)
# перетворення рядків на числа через int()
total_rec = sum(int(p) for p in all_perms)

print(f"  кількість: {count_rec}")
print(f"  сума:      {total_rec}")

# підсумок
print("\n" + "=" * 55)
print("підсумок (всі способи дають однаковий результат):")
print(f"  кількість п'ятизначних чисел: {count_fact}")
print(f"  сума всіх чисел:              {total_fact}")