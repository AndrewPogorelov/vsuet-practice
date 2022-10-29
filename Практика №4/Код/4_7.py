
n = int(input("Введите число n: "))
prev_fact = 1
summ_fact = 0
for miss_mult in range(1, n+1):
    curr_fact = prev_fact * miss_mult
    summ_fact += curr_fact
    prev_fact = curr_fact
print(summ_fact)
