"""

Для списку list_3 виконати такі дії із використанням спискових
включень та/або функціq map():
 сформувати з нього список list_4, що складається тільки із чисел;
 вивести всі додатні елементи списку list_4 із використанням спискових
включень,
 виконати попередній пункт за допомогою функцій map(), filter();
 створити список квадратів елементів списку list_4
 вивести елементи списку list_3, які є літерами, у верхньому регістрі із
використанням спискових включень;
 виконати попередній пункт за допомогою функцій map(), filter().

"""
list_3 = [3, -5, 7, 'A', ' ', 'b', ' ', 'B', 'd', ' ', '1', '2', 'a', '0', '5', '7', 'c', 'd', 'F', '#']

# формуємо list_4 тільки з чисел (забираємо цілі числа та цифри з рядка)
list_4 = [int(x) for x in list_3 if isinstance(x, int) or (isinstance(x, str) and x.lstrip('-').isdigit())]
print("список list_4 (лише числа):", list_4)

# виведення додатних елементів за допомогою спискових включень
positive_comp = [x for x in list_4 if x > 0]
print("додатні елементи (спискове включення):", positive_comp)

# виведення додатних елементів за допомогою filter()
positive_filter = list(filter(lambda x: x > 0, list_4))
print("додатні елементи (filter):", positive_filter)

# список квадратів елементів list_4
squares = [x**2 for x in list_4]
print("квадрати елементів list_4:", squares)

# літери з list_3 у верхньому регістрі (спискове включення)
letters_upper_comp = [x.upper() for x in list_3 if isinstance(x, str) and x.isalpha()]
print("літери у верхньому регістрі (включення):", letters_upper_comp)

# літери з list_3 у верхньому регістрі за допомогою map() та filter()
letters_upper_map = list(map(lambda x: x.upper(), filter(lambda x: isinstance(x, str) and x.isalpha(), list_3)))
print("літери у верхньому регістрі (map/filter):", letters_upper_map)