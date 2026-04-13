"""
Задано рядок. Вивести рядок в зворотному порядку із використанням:
 слайсів;
 циклу for;
 циклу while
 методу списків list.reverse()
"""

# вхідний рядок
s = input("введіть рядок: ")

# --- спосіб 1: слайс ---
reversed_slice = s[::-1]
print(f"слайс:          {reversed_slice}")

# --- спосіб 2: цикл for ---
reversed_for = ""
for char in s:
    reversed_for = char + reversed_for
print(f"for:            {reversed_for}")

# --- спосіб 3: цикл while ---
reversed_while = ""
i = len(s) - 1
while i >= 0:
    reversed_while += s[i]
    i -= 1
print(f"while:          {reversed_while}")

# --- спосіб 4: list.reverse() ---
chars = list(s)
chars.reverse()
reversed_list = "".join(chars)
print(f"list.reverse(): {reversed_list}")