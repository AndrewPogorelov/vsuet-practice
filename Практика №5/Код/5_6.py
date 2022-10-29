#Определите среднее значение всех элементов последовательности, завершающейся числом 0.

from statistics import mean

X = int(input("Введите число: "))
count = 1
sum_number = X
while X != 0:
    count += 1
    X = int(input("Введите число: "))
    sum_number += X
print("среднее значение всех элементов:", sum_number/count)
