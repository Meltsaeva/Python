# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

string_1 = str(input("Input string - "))
simbols = string_1.split()
string_2 = []
count = {}
for i in simbols:
    if i not in count:
        count[i] = 0
    else:
        count[i] += 1
    if count[i] > 0:
        string_2.append(f"{i}_{count[i]}")
    else:
        string_2.append(i)
string_2 = ' '.join(string_2)
print(string_2)