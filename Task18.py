# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input("Input N - "))
list_1 = []
for i in range(n):
    a = int(input("Input a - "))
    list_1.append(a)
number = int(input("Input the number - "))
x = list_1[0]
min_diff = abs(list_1[0] - number)
for i in range(len(list_1)):
    diff = abs(list_1[i]  - number)
    if diff < min_diff:
        min_diff = diff
        x = list_1[i]
print(x)
