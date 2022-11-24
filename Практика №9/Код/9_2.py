# В данной действительной квадратной матрице порядка n найти наибольший по модулю элемент
# получить квадратную матрицу порядка n - 1 путем отбрасывания из исходной матрицы строки и столбца,
# на пересечении которых расположен элемент с найденным значением.

n=int(input('Введите количество строк: '))
l=[]
for i in range(n):
    l1=[int(j) for j in input('Введите '+str(i+1)+'-ю строку: ').split()]
    l.append(l1)
m=-9999999999999999999
for i in range(len(l)):
    if m<max(l[i]):
        m=max(l[i])
        ind1=i
        ind2=l[i].index(m)
for i in range(len(l)):
    if i!=ind1:    
        for j in range(len(l[i])):
            if j!=ind2:
                print(l[i][j],end=' ')
        print()