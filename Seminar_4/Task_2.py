# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

def Factor(N):
    List = []
    d = 2
    while d * d <= N:
        if N % d == 0:
            List.append(d)
            N //= d
        else:
            d += 1
    if N > 1:
        List.append(N)
    return List
print(Factor(int(input("Введите число: "))))
