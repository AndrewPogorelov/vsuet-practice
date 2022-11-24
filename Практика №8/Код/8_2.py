# Даны 3 различных массива целых чисел. В каждом массиве найти произведение
# элементов и среднеарифметическое значение.

m1=[int(i) for i in input('Введите первый масив ').split()]
m2=[int(i) for i in input('Введите второй масив ').split()]
m3=[int(i) for i in input('Введите третий масив ').split()]
def poisk(m):
    p=m[0]
    s=m[0]
    for i in range(1,len(m)):
        p*=m[i]
        s+=m[i]
    print('Произведение массива',p,'Среднеарифметическое', s/len(m))
poisk(m1)
poisk(m2)
poisk(m3)