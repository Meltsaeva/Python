# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

def numbers(a, b):
    if b == 0:
        return 1
    else:
        return a * numbers(a, b - 1)

a = int(input("Input A - "))
b = int(input("Input B - "))
print(numbers(a, b))

