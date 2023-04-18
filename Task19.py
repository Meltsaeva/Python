# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

k = int(input("Input K - "))
n = int(input("Input N - "))
list = []
for i in range(n):
    x = int(input("Input x - "))
    list.append(x)
print(list)
for i in range(k):
    list.insert(0, list.pop())
# print(*list[-k:], *list[:len(list) - k])
print(*list)
