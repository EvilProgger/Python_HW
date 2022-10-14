# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.

upper = int(input("Введите верхнюю границу диапазона: "))
list = [i for i in range(20, upper + 1) if i % 20 == 0 or i % 21 == 0]

print("Список чисел кратных 20 или 21 в диапазоне от 20 до", upper , list)