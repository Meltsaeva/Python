# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
n = int(input("Input N - "))
list_1 = []
for i in range(n):
    x = int(input("Input x - "))
    list_1.append(x)
number = int(input("Input the number - "))
count = list_1.count(number)
print(count)