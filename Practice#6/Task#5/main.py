"""
Задано рядок слів розподілених пробілом. Вивести рядок зі словами в
зворотному порядку із використанням:
 циклу while та умовного оператору if
 методів рядків та списків (split, reverse)
Наприклад, заданий рядок “функції та методи роботи із рядками”. На
виході отримати рядок “рядками із роботи методи та функції”

"""

# вхідний рядок
s = input("введіть рядок слів: ")

# --- спосіб 1: цикл while та умовний оператор if ---
words = []
current = ""
i = 0
while i < len(s):
    if s[i] != " ":
        # накопичення символів поточного слова
        current += s[i]
    else:
        if current:
            words.append(current)
            current = ""
    i += 1
# додавання останнього слова
if current:
    words.append(current)

# збирання слів у зворотному порядку
reversed_while = ""
j = len(words) - 1
while j >= 0:
    reversed_while += words[j]
    if j > 0:
        reversed_while += " "
    j -= 1
print(f"while + if: {reversed_while}")

# --- спосіб 2: split та reverse ---
word_list = s.split()
word_list.reverse()
reversed_split = " ".join(word_list)
print(f"split + reverse: {reversed_split}")