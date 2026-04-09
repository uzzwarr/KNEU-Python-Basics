"""

Напишіть програму для створення словника із введеного рядка
символів для підрахунку кількості символів: ключами є букви, значеннями
кількість входжень. Знаки пунктуації та пробіли включати не потрібно,
великі та маленькі літери вважаються однаковими
“Take the first step in faith. You don’t have to see the whole
staircase, just take the first step. Only two things are infinite — the
universe and human stupidity, and I’m not sure about the former”
 Знайдіть довжину словника та виведіть на друк усі пари ключ-
значення;
 визначте, скільки разів зустрічались літери a, j;
 знайдіть букву, що найчастіше та найрідше зустрічалася у цьому
рядку;
 якщо деякі з літер не зустрічались, додайте їх до словника зі значенням
0.

"""

import string

text = "Take the first step in faith. You don’t have to see the whole staircase, just take the first step. Only two things are infinite — the universe and human stupidity, and I’m not sure about the former"

# створюємо словник для підрахунку (тільки літери, нижній регістр)
char_counts = {}
for char in text.lower():
    if char.isalpha(): # відсікаємо пробіли та знаки пунктуації
        char_counts[char] = char_counts.get(char, 0) + 1

# довжина словника та всі пари
print("довжина словника:", len(char_counts))
print("пари ключ-значення:")
for k, v in char_counts.items():
    print(f"'{k}': {v}")

# скільки разів зустрічалися 'a' та 'j'
print("\nкількість 'a':", char_counts.get('a', 0))
print("кількість 'j':", char_counts.get('j', 0))

# найчастіша та найрідкісніша літери
most_freq = max(char_counts, key=char_counts.get)
least_freq = min(char_counts, key=char_counts.get)
print("\nнайчастіша літера:", most_freq, f"({char_counts[most_freq]} разів)")
print("найрідкісніша літера:", least_freq, f"({char_counts[least_freq]} разів)")

# додаємо літери алфавіту, яких не було, зі значенням 0
for char in string.ascii_lowercase:
    if char not in char_counts:
        char_counts[char] = 0

print("\nсловник після додавання відсутніх літер:")
print(char_counts)