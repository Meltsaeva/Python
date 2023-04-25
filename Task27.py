# Хакер Василий получил доступ к классному журналу и хочет заменить все свои 
# минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, 
# но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1

# import random
# list_1 = random.randint(1, 1, 5)
# print(list_1)

# n = int(input("Input the number of grades -"))
# for i in range(n):
#     m = int(input("Input a grade -"))
#     list_1

n = int(input("Введите число: "))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

factorial(n)
print(f"Факториал числа {n} -  {factorial(n)}")
