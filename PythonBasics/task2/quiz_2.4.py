"""
Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки нужно пронумеровать.
Если слово длинное, выводить только первые 10 букв в слове.
"""

userString = input('Введите строку из нескольких слов через пробел.\n')
userWords = userString.split(" ")

for word in userWords:
    print(word[0:10], end="\n")
