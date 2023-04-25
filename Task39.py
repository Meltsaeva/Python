# определить является ли слово полиндромом при помощи рекурсии

# str1 = input("Input - ")
# def pal(str1):
#     if len(str1) == 0 or len(str1) == 1:
#         return True
#     if str1[0] == str1[-1]:
#         return pal(str1[1:-1])
#     else:
#         return False


# print(pal(str1))

# Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве),
# которых нет во втором массиве. Пользователь вводит число N - 
# количество элементов в первом массиве, затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива

# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1
# Вывод:
# 3 3 2 12

n = int(input("Input N - "))
array_1 = [int(input(f'Input {i} ' ))for i in range(n)]    
m = int(input("Input M - "))
array_2 = [int(input(f'Input {i} ' ))for i in range(m)]    
for i in range(n):
    if array_1[i] not in array_2:
        print(array_1[i], end = " ")
    