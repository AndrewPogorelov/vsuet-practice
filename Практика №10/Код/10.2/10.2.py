# В данной действительной квадратной матрице порядка n найти наибольший по модулю элемент
# получить квадратную матрицу порядка n - 1 путем отбрасывания из исходной матрицы строки и столбца,
# на пересечении которых расположен элемент с найденным значением.
with open('pogorelovAV_y223_vvod.txt', 'r') as file:
    k = file.read(1)
    k = int(k)
    l = file.readlines()
l = [[int(n) for n in x.split()] for x in l]
m=-9999999999999999999
print(l)
with open('pogorelovAV_y223_vivod.txt','w') as file:
    for i in range(1,len(l)):
        if m < max(l[i]):
            m=max(l[i])
            ind1=i
            ind2=l[i].index(m)
    for i in range(1,len(l)):
        if i!=ind1:
            for j in range(len(l[i])):
                if j!=ind2:
                    file.write(str(l[i][j]))
                    file.write(' ')
            file.write('\n')