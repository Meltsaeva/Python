# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

n = int(input("Input N - "))
a = 0
b = 1
count = 0
i = 2
t = 0
while (n > count):
    count = a + b
    a = b
    b = count
    if n == count:
        break
    i += 1
if count != n:
    print("-1")
else:
    print(i+1)
    