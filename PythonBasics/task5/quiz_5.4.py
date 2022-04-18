"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
translateTable = {
    'one': 'Один',
    'two': 'Два',
    'three': 'Три',
    'four': 'Четыре'
}

with open('quiz5.4', 'r', encoding='utf-8') as userFile:
    fileLines = [line.split(" ") for line in userFile]
    newFileLines = []
    for line in fileLines:
        line[0] = translateTable[line[0].lower()]
        newFileLines.append(line)
    userFile.close()

with open('quiz5.4_new', 'w', encoding='utf-8') as newFile:
    for line in newFileLines:
        newFile.write(' '.join(line))
    newFile.close()
