# Для целочисленной квадратной матрицы найти число элементов, кратных K,
# и наибольший из этих элементов
with open('pogorelovAV_y223_vvod.txt', 'r') as file:
    k = file.read(1)
    k = int(k)
    l = file.readlines()
l = [[int(n) for n in x.split()] for x in l]
def sss(l,k):
    p = []
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] % k == 0:
                p.append(l[i][j])
    return ( p )
with open('pogorelovAV_y223_vivod.txt', 'w') as file:
    p = sss(l, k)
    p = [str(i) for i in p]
    file.write(' '.join(p))
    file.write('\n')
    file.write(str(max(sss(l,k))))