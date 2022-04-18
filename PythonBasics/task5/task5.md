# Практическое задание. Урок 5
---
[Задание 1](quiz_5.1.py)  
```python
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
```
---
[Задание 2](quiz_5.2.py)  
```python
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
```
---
[Задание 3](quiz_5.3.py)  
```python
"""
Создать текстовый файл (не программно).
Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
"""

with open('quiz5.1', 'r', encoding='utf-8') as userFile:
    fileLines = [line.rstrip().split(" ") for line in userFile]
    employeeCount = len(fileLines)
    print('Фамилии сотрудников с окладом менее 20 тысяч:')
    totalSalary = 0
    for emp in fileLines:
        if float(emp[2]) < 20000:
            print(emp[0])
        totalSalary += float(emp[2])
    print('Средний доход сотрудников: %0.2f' % (totalSalary/employeeCount))
    userFile.close()
```
---
[Задание 4](quiz_5.4.py)  
```python
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
```
---
[Задание 5](quiz_5.5.py)  
```python
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
```
---
[Задание 6](quiz_5.6.py)  
```python
"""
Сформировать (не программно) текстовый файл.
В нём каждая строка должна описывать учебный предмет и
наличие лекционных, практических и лабораторных занятий по предмету.
Сюда должно входить и количество занятий.
Необязательно, чтобы для каждого предмета были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести его на экран.
Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def countHours(rawData):
    totalHours = 0
    for entry in rawData:
        try:
            activityTime = int(entry.split("(")[0])
            totalHours += activityTime
        except ValueError:
            pass
    return totalHours


coursesSerialized = {}
with open('quiz5.6', 'r', encoding='utf-8') as coursesFile:
    fileLines = coursesFile.read().split("\n")
    for course in fileLines:
        if (len(course) != 0):
            course = course.split(":")
            courseName = course.pop(0)
            courseHours = countHours(course[0].split(" "))
            coursesSerialized[courseName] = courseHours
    coursesFile.close()

print(coursesSerialized)
```
---
[Задание 7](quiz_5.7.py)  
```python
"""
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

firmsProfit = {}
with open("quiz5.7", 'r', encoding='utf-8') as sourceFile:
    while True:
        firmInfo = sourceFile.readline()
        if not firmInfo:
            break
        [name, form, income, outcome] = firmInfo.split(" ")
        firmsProfit[name] = int(income) - int(outcome)
    sourceFile.close()

averageProfit = 0
firmsWithProfit = 0
for profit in firmsProfit.values():
    if profit > 0:
        firmsWithProfit += 1
        averageProfit += profit
statData = [firmsProfit, {"average_profit": averageProfit/firmsWithProfit}]


with open('res5.7.json', 'w', encoding='utf-8') as resFile:
    json.dump(statData, resFile, ensure_ascii=False)
    resFile.close()
```
