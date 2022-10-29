n = int(input("Введите количество ступенек: "))
for step_num in range(1, n+1):
    for num in range(1, step_num+1):
        print(num, end='')
    print(end="\n")
