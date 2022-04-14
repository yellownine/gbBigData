"""
Поработайте с переменными, создайте несколько, выведите на экран.
Запросите у пользователя некоторые числа и строки и сохраните в переменные, затем выведите на экран.
"""

integerVariable = 2
stringVariable = '2'
array = [integerVariable, stringVariable]
dict = {stringVariable: integerVariable}

print('Угадайте, какая из переменных строковая: 1) ' + str(integerVariable) + ' 2) ' + stringVariable)
strVarchoice = input()

print('А какая целочисленная: 1) ' + str(integerVariable), '2) ' + stringVariable)
intVarchoice = input()

print('Согласен, вопрос сложный и даже некорректный.')

userName = input('Простите, я даже не спросил, как вас зовут?\n')
print('Привет, %s!' % userName)
