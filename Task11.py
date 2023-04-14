# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# a = 0
# b = 1
# n = int(input("Input N - "))
# sum = 0
# i = 1
# while (sum <= n):
#     sum = a + b
#     a = b
#     b = sum
#     i += 1
#     if n != sum:
#         print("-1")
#         break
#     else:print(i)

a = 0
b = 1
n = int(input("Input N - "))
sum = 0
i = 1
while (sum <= n):
    sum = a + b
    a = b
    b = sum
    i += 1
if n != sum:
    print("-1")
else: print(i)