"""
Для списка реализовать обмен значений соседних элементов.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
При нечётном количестве элементов последний сохранить на своём месте.
Для заполнения списка элементов нужно использовать функцию input().
"""

userArray = []
chnagedUserArray = []

while True:
    userElement = input('Введите что-нибудь. Когда надоест, просто нажмите Enter. ')
    if userElement == '':
        break
    else:
        userArray.append(userElement)

while len(userArray) > 1:
    chnagedUserArray.append(userArray.pop(1))
    chnagedUserArray.append(userArray.pop(0))

chnagedUserArray += userArray
print(chnagedUserArray)
