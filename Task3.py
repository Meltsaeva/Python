# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

a = int(input("Input number of students in the class A - "))
b = int(input("Input number of students in the class B - "))
c = int(input("Input number of students in the class C - "))

print(((a+1)//2+(b+1)//2+(c+1)//2))