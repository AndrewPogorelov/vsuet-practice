# Вариант 9
def l():
    N = int(input("Введите число N: "))

    print("Введите список- ")
    list_1 = [int(input()) for index in range(N)]

    list_abs=[]
    for index in range(len(list_1)):
        list_abs.append(abs(list_1[index]))
    print("Минимальный элемент- ", min(list_abs))


    list_1.reverse()
    print("Обратный список-", list_1)
l()