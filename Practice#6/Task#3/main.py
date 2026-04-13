"""
Задано рядок, що містить натуральні числа та слова. Необхідно
сформувати список із чисел!!!, що містяться в цьому рядку:
 із використанням циклу for
 із використанням циклу while
Наприклад, заданий рядок "abc83 cde7 1 b 24". На виході ми маємо
отримати список [83, 7, 1, 24].
"""

# вхідний рядок
s = input("введіть рядок: ")

# --- спосіб 1: цикл for ---
numbers_for = []
current = ""
for char in s:
    if char.isdigit():
        # накопичення цифр поточного числа
        current += char
    else:
        if current:
            numbers_for.append(int(current))
            current = ""
# додавання останнього числа, якщо рядок закінчується цифрою
if current:
    numbers_for.append(int(current))
print(f"for:   {numbers_for}")

# --- спосіб 2: цикл while ---
numbers_while = []
current = ""
i = 0
while i < len(s):
    if s[i].isdigit():
        # накопичення цифр поточного числа
        current += s[i]
    else:
        if current:
            numbers_while.append(int(current))
            current = ""
    i += 1
# додавання останнього числа, якщо рядок закінчується цифрою
if current:
    numbers_while.append(int(current))
print(f"while: {numbers_while}")
