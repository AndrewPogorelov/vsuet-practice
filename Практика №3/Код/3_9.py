# ЗАДАЧА №9
# Шоколадка имеет вид прямоугольника, разделенного на n×m долек.
# Шоколадку можно один раз разломить по прямой на две части.
# Определите, можно ли таким образом отломить от шоколадки часть, состоящую ровно из k долек.
# Программа получает на вход три числа: n, m, k и должна вывести "Да" или "Нет".

print('Введите дольки шоколадки:')
n = int(input())
m = int(input())
k = int(input())
if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('нет')
else:
    print('да')
