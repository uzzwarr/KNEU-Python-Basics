"""
2.	Дано тризначне число.
	піднести це число до 3-го ступеня. Вважаючи, що результат – це розмір файлу кілобайтах, використовуючи операцію ділення націло,
визначити, скільки це буде повних мегабайт, гігабайт
	у ньому закреслили першу зліва цифру і приписали її справа. Вивести отримане число;
	знайти суму і добуток його цифр;
	вивести число, отримане при перестановці цифр сотень і десятків вихідного числа (наприклад, 123 перейде в 213).
"""
number = int(input("Введіть трьохзначне число: "))

kb = number ** 3
mb = kb // 1024
gb = mb // 1024

print("Розмір у кілобайтах: ", kb)
print("Повних мегабайт: ", mb)
print("Повних гігабайт: " ,gb)

first_digit = number // 100
remainder = number % 100
new_number = remainder * 10 + first_digit
print(new_number)

second_digit = remainder // 10
third_digit = remainder % 10

print(first_digit + second_digit + third_digit)
print(first_digit * second_digit * third_digit)

print((second_digit * 100) + (first_digit * 10) + third_digit)
