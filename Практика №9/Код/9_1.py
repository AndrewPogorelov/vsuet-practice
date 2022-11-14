# Для целочисленной квадратной матрицы найти число элементов, кратных K,
# и наибольший из этих элементов

k=int(input('Введите k: '))
n=int(input('Введите количество строк: '))
l=[]
p=[]
for i in range(n):
    l1=[int(j) for j in input('Введите '+str(i+1)+'-ю строку: ').split()]
    l.append(l1)
for i in range(len(l)):
    for j in range(len(l[i])):
        if l[i][j]%k==0:
            p.append(l[i][j])
            print(l[i][j],end=' ')
print()
print('Максимальное из кратных: ',max(p))
        
