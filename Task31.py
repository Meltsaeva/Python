# Последовательностью Фибоначчи называется последовательность 
# чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1). 
# Требуется найти N-е число Фибоначчи
# Input: 7 Output: 21

n = int(input("Input N - "))
def fibonacci(n): 
    if n == 0:
        return 0
    elif n == 1:
            return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(n))