# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

array = []
a1 = int(input("Input a1 - "))
d = int(input("Input d - "))
n = int(input("Input N - "))
i = 0
for i in range(n):
    an = a1 + i * d
    array.append(an)
print(array)