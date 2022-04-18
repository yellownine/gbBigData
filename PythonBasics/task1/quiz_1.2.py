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
