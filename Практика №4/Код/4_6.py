# Факториалом числа n называется произведение 1 x 2 x ... x n.
# Обозначение: n!. По данному натуральному n вычислите значение n!.
# Пользоваться математической библиотекой math в этой задаче запрещено.

n = int(input("Введите число n!: "))
sum_fact = 1
for number in range(2, n+1):
    sum_fact *= number
print("Факториал числа " + str(n) + " = " + str(sum_fact))
