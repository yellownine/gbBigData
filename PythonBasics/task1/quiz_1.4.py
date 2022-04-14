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
