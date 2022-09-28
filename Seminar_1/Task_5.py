# 5. Напишите программу, которая принимает на вход координаты
#    двух точек и находит расстояние между ними в 2D пространстве.
#    https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
print("Нахождение расстояния между точками", "\nПервая точка: ")
x_1 = int(input("Введите X1"))
y_1 = int(input("Введите Y1"))
print("Вторая точка: ")
x_2 = int(input("Введите X2"))
y_2 = int(input("Введите Y2"))

print(f"{((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** 0.5:0.4}")
