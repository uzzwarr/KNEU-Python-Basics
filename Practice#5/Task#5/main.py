"""

Створіть словник для зберігання інформації про міста. Використайте
назви міст в якості ключів словника. Створіть словник з інформацією про
кожне місто: включіть в нього країну, в якій розташоване місто, приблизну
чисельність населення і один цікавий факт про місто. Виведіть назву
кожного міста і всю збережену інформацію про нього як у вихідних даних.

 На основі цього словника створіть інший словник, що зберігає пари
ключ-значення у вигляді «країна: столиця»;
 напишіть програму для сортування за зростанням словника за
значеннями.Інформація виводиться як у вихідних даних: сортування
має бути проведено за назвами столиць.
Примітка. При використанні метода sorted, можна застосувати як ключ лямбда-функцію на
зразок key=lambda x: x[1]

"""

# словник з інформацією про міста
cities = {
    "Rome": {
        "Country": "Italy",
        "Population": "2868000 people",
        "Fact": 'Rome is one of the oldest cities in the world, the capital of Ancient Rome. Therefore, Rome is often called the "eternal city".'
    },
    "Canberra": {
        "Country": "Australia",
        "Population": "381448 people",
        "Fact": 'The design of Canberra was based on the concept of a garden city, which includes significant areas of natural vegetation, which earned for Canberra the title of "bush capital" (translated from the English "forest capital").'
    },
    "Toronto": {
        "Country": "Canada",
        "Population": "2503281 people",
        "Fact": 'In the world of professional sports, the city is the most famous hockey team of Toronto Maple Leafs. The city holds the nickname of the "hockey universe center".'
    }
}

# виведення початкового словника згідно з прикладом
for city, info in cities.items():
    print(f"{city}:")
    for key, value in info.items():
        print(f"  {key}: {value}")
    print()

# створюємо новий словник «країна: столиця» (в рамках завдання міста виступають столицями)
country_capital = {info["Country"]: city for city, info in cities.items()}

# сортування словника за значеннями (за назвами столиць) по зростанню
sorted_capitals = dict(sorted(country_capital.items(), key=lambda item: item[1]))

print("відсортований список (країна: столиця):")
for country, capital in sorted_capitals.items():
    print(f"{country}: {capital}")