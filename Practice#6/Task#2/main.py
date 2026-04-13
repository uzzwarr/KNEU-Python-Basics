"""
Задано рядок, що містить натуральні числа та слова. Необхідно
сформувати список із цифр, що містяться в цьому рядку:
 із використанням циклу for
 із використанням циклу while
 спискового включення
Наприклад, заданий рядок "abc83 cde7 1 b 24". На виході ми маємо
отримати список [8, 3, 7, 1, 2, 4].
"""

# вхідний рядок
s = input("введіть рядок: ")

# --- спосіб 1: цикл for ---
digits_for = []
for char in s:
    if char.isdigit():
        digits_for.append(int(char))
print(f"for:    {digits_for}")

# --- спосіб 2: цикл while ---
digits_while = []
i = 0
while i < len(s):
    if s[i].isdigit():
        digits_while.append(int(s[i]))
    i += 1
print(f"while:  {digits_while}")

# --- спосіб 3: спискове включення ---
digits_comp = [int(c) for c in s if c.isdigit()]
print(f"спискове включення: {digits_comp}")