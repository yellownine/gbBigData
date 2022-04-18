"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

sourceData = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


# 1
def filterArray(array):
    result = []
    for i in range(1, len(array)):
        first = array[i-1]
        second = array[i]
        if second > first:
            result.append(second)
    return result


# 2
result = [sourceData[i] for i in range(1, len(sourceData)) if sourceData[i] > sourceData[i-1]]


print(filterArray(sourceData))
print(result)
