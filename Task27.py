# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13

# string_1 = set(str(input("Input string - ")).lower())
# print(len(string_1), string_1)
text = str(input("Input string - ").lower())
string_1 = set(text.split())
print(len(string_1))