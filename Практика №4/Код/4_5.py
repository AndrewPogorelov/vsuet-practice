# По данному натуральному n вычислите сумму 1^3+2^3+3^3...+n^3

N = int(input("Введите число n: "))
number = 0
sum_number = 0
while number < N:
    number += 1
    sum_number += number**3
print(sum_number)
