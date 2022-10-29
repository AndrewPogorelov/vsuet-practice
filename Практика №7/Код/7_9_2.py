# Вариант 9

print("Введите список A:")
list_A = [int(input()) for index1 in range(10)]

print("Введите список B:")
list_B = [int(input()) for index2 in range(10)]

print("Первый массив- ", list_A, "\n", "Второй массив- ", list_B)

list_c = list_B
list_B = list_A.copy()
list_A = list_c.copy()
print("Первый преобразованный массив- ", list_A, "\n", "Второй преобразованный массив- ", list_B)
