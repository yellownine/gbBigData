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