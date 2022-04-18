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
