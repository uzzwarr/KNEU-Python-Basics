"""
Напишіть функцію з використанням функції enumerate(), яка приймає
 список чисел і повертає список індексів та їхніх значень, які більше 10;
 список слів і повертає словник, де ключами є слова, а значеннями - їхні
індекси;
 список чисел і визначає, чи є серед них парні числа, та повертає список
кортежів індексів та парних чисел;
 рядок та повертає список рядків, розділених за пропусками, разом із
їхніми індексами;
 список імен та повертає список індексів та імен, які починаються на
певну літеру.
"""


# індекси та значення більше 10
def indices_greater_than_10(numbers):
    """повертає список (індекс, значення) для елементів більших за 10."""
    result = []
    for i, val in enumerate(numbers):
        if val > 10:
            result.append((i, val))
    return result


# словник {слово: індекс}
def words_to_index_dict(words):
    """повертає словник, де ключ — слово, значення — його індекс у списку."""
    return {word: i for i, word in enumerate(words)}


# кортежі (індекс, парне число)
def even_with_indices(numbers):
    """повертає список кортежів (індекс, значення) для парних елементів."""
    result = []
    for i, val in enumerate(numbers):
        if val % 2 == 0:
            result.append((i, val))
    return result


# слова рядка з їхніми індексами
def string_words_with_indices(text):
    """розбиває рядок на слова та повертає список (індекс, слово)."""
    result = []
    for i, word in enumerate(text.split()):
        result.append((i, word))
    return result


# імена, що починаються на задану літеру, з індексами
def names_starting_with(names, letter):
    result = []
    for i, name in enumerate(names):
        if name.lower().startswith(letter.lower()):
            result.append((i, name))
    return result


raw_nums = input("введіть числа через пробіл (для пошуку > 10): ").split()
nums = [int(x) for x in raw_nums]
print(f"список чисел: {nums}")
print("індекси та значення > 10:", indices_greater_than_10(nums))

# введення слів для словника
raw_words = input("\nвведіть слова через пробіл для словника {{слово: індекс}}: ").split()
print("словник {слово: індекс}:", words_to_index_dict(raw_words))

# введення чисел для пошуку парних
raw_nums2 = input("\nвведіть числа через пробіл для пошуку парних: ").split()
nums2 = [int(x) for x in raw_nums2]
print(f"список чисел: {nums2}")
print("парні з індексами:", even_with_indices(nums2))

# введення рядка для розбиття на слова з індексами
text = input("\nвведіть рядок для розбиття на слова з індексами: ")
print("слова з індексами:", string_words_with_indices(text))

# введення імен та літери для фільтрації
raw_names = input("\nвведіть імена через пробіл: ").split()
letter = input("введіть літеру для пошуку імен: ")
print(f"імена що починаються на '{letter}':", names_starting_with(raw_names, letter))