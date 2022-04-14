# Практическое задание. Урок 1
---
[Задание 1](quiz_1.1.py)
```python
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
```
---
[Задание 2](quiz_1.2.py)  
```python
"""
Пользователь вводит время в секундах.
Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
"""
import helpers


def convertSecsToHhMmSs(intTimeInSecs):
    secs = intTimeInSecs % 60
    mins = (intTimeInSecs - secs) / 60 % 60
    hours = ((intTimeInSecs - secs) / 60 - mins) / 60 % 60
    return {
        'hh': hours,
        'mm': mins,
        'ss': secs
    }


timeInSecs = helpers.getUserNumber('Введите время в секундах, я переведу его в другой формат: ')
formatedTime = convertSecsToHhMmSs(timeInSecs)
print(
    'Вы провели в цирке Монти Пайтона %dч:%dм:%dс. Ждем вас снова!'
    % (formatedTime['hh'], formatedTime['mm'], formatedTime['ss'])
)
```
---
[Задание 3](quiz_1.3.py)  
```python
"""
Узнайте у пользователя число n.
Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3.
Считаем 3 + 33 + 333 = 369.
"""
import helpers


def elevenizeNumber(n):
    n = str(n)
    return int(n) + int(n + n) + int(n + n + n)


userNum = helpers.getUserNumber('Введите чилсло: ')

print('Я превратил ваше число в %d' % elevenizeNumber(userNum))
```
---
[Задание 4](quiz_1.4.py)  
```python
"""
Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
import helpers


userNum = helpers.getUserNumber('Введите какое-нибудь число, можно большое: ')
needToIterate = userNum >= 10
maxDigit = userNum % 10

while needToIterate:
    userNum = userNum // 10
    maxDigit = maxDigit if maxDigit > userNum % 10 else userNum % 10
    needToIterate = userNum >= 10

print('Самая большая цифра в вашем числе: %d!' % maxDigit)
```
---
[Задание 5](quiz_1.5.py)  
```python
"""
Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма.
Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки. Выведите соответствующее сообщение.

Если фирма отработала с прибылью, вычислите рентабельность выручки.
Это отношение прибыли к выручке. Далее запросите численность сотрудников фирмы и
определите прибыль фирмы в расчёте на одного сотрудника.
"""
import helpers


income = helpers.getUserNumber('Введите значение выручки вашей фирмы: ')
outcome = helpers.getUserNumber('Введите значение издержек вашей фирмы: ')
effect = income - outcome

if effect == 0:
    effectMsg = 'нулевой прибылью, но и убытков нет'
elif effect > 0:
    effectMsg = 'прибылью %d' % effect
    rent = effect / income
    empCount = helpers.getUserNumber('Сколько сотрудников в вашей фирме?: ')
    effectToOneEmp = effect / empCount
    print('Рентабельность вашей фирмы %.3f' % rent)
    print('Прибыль, пересчитанная на одного сотрудника, %.3f' % effectToOneEmp)
elif effect < 0:
    effectMsg = 'убытком %d' % effect
```
---
[Задание 6](quiz_1.6.py)  
```python
"""
Спортсмен занимается ежедневными пробежками.
В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10% относительно предыдущего.
Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3. Результат:
1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на шестой день спортсмен достиг результата — не менее 3 км.
"""
import helpers


a = helpers.getUserNumber('Сколько км вы пробежали сегодня: ')
while a <= 0:
    print('Так не пойдет, надо с чего-то начинать!')
    a = helpers.getUserNumber('Сколько км вы пробежали сегодня: ')

b = helpers.getUserNumber('Сколько км вы хотите пробежать: ')
c = a
days = 0
while c < b:
    days += 1
    c = c * 1.1
    print('Беги, ты молодец! У тебя получится!\n')

print('Через %d дней ты достигнешь результата' % days)
```
