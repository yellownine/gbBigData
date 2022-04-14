"""
Продолжить работу над заданием. В программу должна попадать строка из слов,
разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Используйте написанную ранее функцию int_func().
"""
import imp
import sys

inputArgs = sys.argv

capitalizer = imp.load_source('quiz_3.6', 'quiz_3.6.py').int_func

wordsArray = inputArgs[1: -1]

result = ""
for word in wordsArray:
    result += capitalizer(word) + " "

print(result)
