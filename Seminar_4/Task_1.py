# Вычислить число c заданной точностью d

from decimal import Decimal

number = input("Введите число: ")
accuracy = Decimal(number)
accuracy = accuracy.quantize(Decimal(input("Введите точность: ")))
print(accuracy)




