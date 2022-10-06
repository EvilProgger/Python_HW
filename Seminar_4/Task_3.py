# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности в том же порядке.

import random

num = []

def create_list():

    y = 1
    m = int(input("Количество элементов списка: "))
    while y <= m:
        num.append(random.randrange(1, 10))
        y += 1
    print("Сгенерированный список:", num)

def non_repeating_nums():
    print("Неповторяющиеся элементы:")
    for i in num:
        if num.count(i) == 1:
            print(i, end= " ")

create_list()
non_repeating_nums()



