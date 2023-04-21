# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.

# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input("Input N - "))
m = int(input("Input M - "))
list_1 = []
list_2 = []
list_3 = []

for i in range(n):
    x = int(input("Input x - "))
    list_1.append(x)

for j in range(m):
    y = int(input("Input y - "))
    list_2.append(y)

# list_1 = list(set(list_1))
# list_2 = list(set(list_2))

# new_list = list_1.extend(list_2)

# for i in set(list_1):

# low_index = m if m > n else n
duplicates = []
for i in range(n):
    if list_1[i] in list_2:
        duplicates.append(list_1[i])
duplicates = set(duplicates)
print(duplicates)



