# Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4 

def sum_1(a, b):
    if a == 0:
        return b
    else:
        return sum_1(a - 1, b + 1)


a = int(input("Input A - "))
b = int(input("Input B - "))
print(sum_1(a, b))
