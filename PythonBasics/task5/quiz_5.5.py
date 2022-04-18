"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
import random

fileName = 'quiz5.5'

with open(fileName, 'w', encoding='utf-8') as newFile:
    randSeq = [str(random.lognormvariate(3, 10)) for i in range(1, 100)]
    newFile.write(' '.join(randSeq))
    newFile.close()


with open(fileName, 'r', encoding='utf-8') as sourceFile:
    numSeq = [float(num) for num in sourceFile.read().rstrip().split(' ')]
    print(f'Сумма чисел в файле {sum(numSeq)}')
    sourceFile.close()
