n = float(input("Введите вещественное число: "))

def digit_sum(n):
    return sum(map(int, list(str(n).replace('.',''))))

print(n)
print("Сумма цифр введённого числа: ", digit_sum(n))