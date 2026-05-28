import sys, io, math
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
 
# ============================================================
# завдання 1. цикли: сума діапазону, факторіал, просте число
# ============================================================
 
 
def sum_range(start, end):
    # перевіряємо коректність меж діапазону
    if start > end:
        return "помилка: start має бути <= end"
    total = 0
    # підсумовуємо всі числа від start до end включно
    for x in range(start, end + 1):
        total += x
    return total
 
 
def factorial(n):
    # факторіал визначений лише для невід'ємних цілих
    if not isinstance(n, int) or n < 0:
        return "помилка: n має бути невід'ємним цілим числом"
    result = 1
    # множимо всі числа від 1 до n
    for i in range(1, n + 1):
        result *= i
    return result
 
 
def is_prime(n):
    # числа менше 2 простими не вважаються
    if n < 2:
        return False
    # перевіряємо подільність лише до кореня з n
    for d in range(2, int(math.isqrt(n)) + 1):
        if n % d == 0:
            return False
    return True
 
 
print("=" * 55)
print("завдання 1. цикли")
print("=" * 55)
 
# 1а — сума чисел у діапазоні
print("\n1a) сума діапазону")
print(f"  [3, 10]  = {sum_range(3, 10)}")     # очікувано 52
print(f"  [10, 3]  = {sum_range(10, 3)}")     # помилка меж
 
# 1б — факторіал числа
print("\n1b) факторіал")
print(f"  5!  = {factorial(5)}")              # 120
print(f"  0!  = {factorial(0)}")              # 1
print(f"  -4! = {factorial(-4)}")             # помилка
 
# 1в — перевірка на простоту
print("\n1c) просте число")
for n in [2, 17, 21, 97, 100]:
    # для кожного числа виводимо результат перевірки
    print(f"  {n:>3} -> {'просте' if is_prime(n) else 'складене'}")
