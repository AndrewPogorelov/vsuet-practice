# Даны два целых числа А и В
# А > В. Выведите все нечётные числа от А до В включительно,
# в порядке убывания
def l():
    A = int(input("Введите число A: "))
    B = int(input("Введите число B: "))

    if A > B:
        for number in range(A, B - 1, -1):
            if number % 2 != 0:
                print(number)
    else:
        print("error")
l()