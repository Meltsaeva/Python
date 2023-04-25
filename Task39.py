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

# n = int(input("Input N - "))
# array_1 = [int(input(f'Input {i} ' ))for i in range(n)]    
# m = int(input("Input M - "))
# array_2 = [int(input(f'Input {i} ' ))for i in range(m)]    
# for i in range(n):
#     if array_1[i] not in array_2:
#         print(array_1[i], end = " ")

# list1 = [i for i in range(3) if i == 1]
# print(list1)
    

# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. 
# Теперь он использует их в качестве серверов "Пегого дудочника". 
# Помогите владельцу фирмы отыскать все зараженные холодильники.

# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр,
#  и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, 
# главное наличие последовательности букв), то холодильник заражен и нужно вывести номер 
# холодильника, нумерация начинается с единицы

# Формат входных данных
# В первой строке подаётся число n – количество холодильников. В последующих 
# n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 
# 5 до  100 символов.

# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. 
# Если таких холодильников нет, ничего выводить не нужно.

# Sample Input 1:
# 6
# 222anton456
# a1n1t1o1n1
# 0000a0000n00t00000o000000n
# gylfole
# richard
# ant0n
# Sample Output 1:
# 1 2 3
# Sample Input 2:
# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample Output 2:
# 1 2 7 8


def fridge(name):
    nik = "anton"
    index = 0
    for i in name:
        if i == nik[index]:
            index += 1
            if index == len(nik):
                return True
    return False

n = int(input("Input the number of fridges - "))
refridge = []
for j in range(n):
    refridge_name = input("Input the name - ")
    if fridge(refridge_name):
        refridge.append(j + 1)
print(refridge)
