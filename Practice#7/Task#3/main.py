"""
Задано рядок слів string_1, розподілених пробілами. Написати
функцію, яка повертає список слів (рядків), що
 починаються з заданої букви. Використовуйте анонімну lambda-
функцію для перевірки, чи починається слово з заданої букви. Функція
запрошує у користувача ввести букву;
 містять задану букву. Використовуйте анонімну lambda-функцію для
перевірки, чи містить слово задану букву;
 мають задану довжину. Використовуйте анонімну lambda-функцію для
обчислення довжини слова;
 записані в зворотному порядку;
 починаються з заданого префіксу prefix, який передається як параметр
у функцію.
"""


# слова, що починаються з заданої букви
def words_starting_with(words):
    letter = input("введіть букву: ").strip().lower()
    # lambda перевіряє першу літеру слова
    check = lambda w: w.lower().startswith(letter)
    return list(filter(check, words))


# слова, що містять задану букву
def words_containing(words, letter):
    """повертає слова, що містять задану букву."""
    check = lambda w: letter.lower() in w.lower()
    return list(filter(check, words))


# слова заданої довжини
def words_of_length(words, length):
    # lambda обчислює довжину та порівнює
    check = lambda w: len(w) == length
    return list(filter(check, words))


# слова у зворотному порядку
def words_reversed(words):
    return words[::-1]


# слова, що починаються з префіксу
def words_with_prefix(words, prefix):
    check = lambda w: w.lower().startswith(prefix.lower())
    return list(filter(check, words))



string_1 = input("введіть рядок слів через пробіл: ")
word_list = string_1.split()
print(f"список слів: {word_list}\n")


print("слова, що починаються з введеної букви:")
print(words_starting_with(word_list))


letter = input("\nвведіть букву для пошуку слів, що її містять: ")
print(f"слова, що містять '{letter}':", words_containing(word_list, letter))


length = int(input("\nвведіть довжину слова для пошуку: "))
print(f"слова довжиною {length}:", words_of_length(word_list, length))


print("\nслова у зворотному порядку:", words_reversed(word_list))

prefix = input("\nвведіть префікс для пошуку слів: ")
print(f"слова з префіксом '{prefix}':", words_with_prefix(word_list, prefix))
