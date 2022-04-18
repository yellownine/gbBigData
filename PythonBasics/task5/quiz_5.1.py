"""
Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""

with open('quiz5.1',  'w', encoding='utf-8') as userFile:
    print('Введите строки, которые хотите добавить в файл.\nЧтобы закончить, введите пустую строку.\n----')
    userLine = input()
    while True:
        if userLine == '':
            userFile.close()
            break
        else:
            userFile.write(userLine)
            userFile.write("\n")
            userLine = input()
