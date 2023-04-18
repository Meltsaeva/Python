# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6



n = int(input("Input the number of elements - "))
list = list()
for i in range(n):
    x = int(input("Input x - "))
    list.append(x)
sum = len(set(list))
print(sum)

