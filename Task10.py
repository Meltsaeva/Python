# На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

h = int(input("Input HEADS - "))
t = int(input("Input TAILS - "))
if h > t:
    print(t)
elif t > h:
    print(h)
else:
    print(t)
