# ЗАДАЧА №1
# Даны два целых чиста A и B (при этом A < Б).
# Выведите все числа от A до B включительно
def l():
    A = int(input("Введите число A: "))
    B = int(input("Введите число B: "))

    if A < B:
        for number in range(A, B+1):
            print(number)
    else:
        print("ERROR")
l()