# Даны два целых числа A и B.
# Выведите все числа от А до В включительно,
# в порядке возрастания, если А < В,
# или в подяке убывания в противном случае.
def l():
    A = int(input("Введите число A: "))
    B = int(input("Введите число B: "))

    if A < B:
        for number in range(A, B + 1):
            print(number)
    else:
        for number in range(A, B - 1, -1):
            print(number)
l()