# Задача No9. Решение в группах
# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * ... * N 
#(произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120

n = int(input("Input N - "))
# sum = n
# while (n > 2 ):
#     sum = sum * (n - 1)
#     n -= 1
# print(sum)

factorial = 1
a = 1
while a <= n:
    factorial = factorial * a
    a += 1
else:
    print(factorial)



