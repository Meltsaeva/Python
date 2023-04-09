# Найдите сумму цифр трехзначного числа. 
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = int(input("Input a number - "))
a = num % 10 
b = num % 100 //10
c = num // 100
print(f" {a + b + c} ({c} + {b} + {a})")
