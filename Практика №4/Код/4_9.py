N = int(input("Введите число N: "))

index = 0
fib_list = [1, 1]
sum_number = 0
if N == 1:
    print(1)
else:
    while index+2 < N:
        fib_list.append(fib_list[index]+fib_list[index+1])
        index += 1
    print("Сумма " + str(N) + "-и чисел Фибоначчи= " + str(sum(fib_list)))
