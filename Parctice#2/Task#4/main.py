x = int(input("Введіть перше ціле число: "))
y = int(input("Введіть друге ціле число: "))
z = int(input("Введіть третє ціле число: " ))

minimum = min(x,y,z)
maximum = max(x, y, z)
medium = x + y + z - maximum - minimum
print(minimum, medium, maximum)
