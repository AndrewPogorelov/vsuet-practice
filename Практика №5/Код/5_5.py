#Программа получает на вход последовательность целых неотрицательных чисел,
# каждое число записано в отдельной строке.
# Последовательность завершается числом 0,
# при считывании которого программа должна закончить свою работу
# и вывести количество членов последовательности
# (не считая завершающего числа 0).
# Числа, следующие за числом 0, считывать не нужно.
def l():
    X = int(input("Введите число: "))
    count = 1
    while X != 0:
        count += 1
        X = int(input("Введите число: "))
    print("Вы ввели", count - 1, "чисел")
l()