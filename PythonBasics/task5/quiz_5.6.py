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
