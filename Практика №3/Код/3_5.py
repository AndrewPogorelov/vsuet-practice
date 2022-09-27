# ЗАДАЧА №5
# Напишите функцию, которая вычисляет наименьшее из трех чисел и выводит на экран.

print('Введите число a:')
a = int(input())

print('Введите число b:')
b = int(input())

print('Введите число c:')
c = int(input())

def f(a,b,c):
    return min(a,b,c)

print('Наименьшее:')
print(f(a,b,c))
