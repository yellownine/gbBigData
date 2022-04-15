"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""
import sys

[hours, rate, premium] = sys.argv[1:4]
try:
    [hours, rate, premium] = [int(hours), float(rate), float(premium)]
except ValueError:
    print('Аргументы скрипта имеют неверный формат')
    sys.exit(1)


def salary(hours, rate, premium):
    return hours * rate + premium


print('Заработная плата сотрудника %0.2f' % salary(hours, rate, premium))
