"""

Дано список значень різних типів даних. Створіть словник із
значеннями списку як ключами, і назвами відповідного типу даних як
значеннями словника. У словнику можуть бути присутні дані одного типу.
Надрукуйте вміст словника як у вихідних даних.

"""


# вхідний список із даними різних типів
data_list = [
    1952, 1000000,
    10.45, 5.5,
    complex(2, 3),
    False,
    "pythonguide.pp.ua",
    (1, -6),
    [3, 15],
    {'Class C': ['Volkswagen Golf', 'Ford Focus'], 'Class F': ['Audi A8', 'Bentley', 'Maybach'], 'E': ['Toyota Camry']},
    {},
    None
]

# створюємо словник, де ключі - типи даних, а значення - список елементів цього типу
type_dict = {}

for item in data_list:
    item_type = type(item)
    if item_type not in type_dict:
        type_dict[item_type] = []
    type_dict[item_type].append(item)

# виведення результату згідно з прикладом
for t, values in type_dict.items():
    # розпаковуємо список значень, щоб вони вивелися через пробіл
    print(t, *values)