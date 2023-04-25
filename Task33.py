# Хакер Василий получил доступ к классному журналу и хочет заменить все свои 
# минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, 
# но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1


def magazine(grades):
    min_grade = min(grades)
    max_grade = max(grades)
    return [min_grade
        if grade == max_grade
        else grade 
            for grade in grades]

n = int(input("Input the number of grades - "))
grades = []
for i in range(n):
    m = int(input("Input the grade - "))
    grades.append(m)

print(magazine(grades))