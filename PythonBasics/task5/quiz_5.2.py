"""
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
"""

with open('quiz5.1', 'r', encoding='utf-8') as userFile:
    fileLines = [line for line in userFile]
    linesCount = len(fileLines)
    print(f'Количество строк в файле {linesCount}')
    wordsCount = {}
    for i in range(0, linesCount):
        wordsInLine = [word for word in fileLines[i].split(" ") if word[0] != "\n" and word[0] != "\t"]
        wordsCount[i+1] = len(wordsInLine)
    print('Количество слов в строках')
    print(wordsCount)
    userFile.close()
