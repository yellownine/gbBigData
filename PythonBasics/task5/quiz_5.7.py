"""
Создать вручную и заполнить несколькими строками текстовый файл,
в котором каждая строка будет содержать данные о фирме: название,
форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
а также словарь со средней прибылью. Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
"""
import json

firmsProfit = {}
with open("quiz5.7", 'r', encoding='utf-8') as sourceFile:
    while True:
        firmInfo = sourceFile.readline()
        if not firmInfo:
            break
        [name, form, income, outcome] = firmInfo.split(" ")
        firmsProfit[name] = int(income) - int(outcome)
    sourceFile.close()

averageProfit = 0
firmsWithProfit = 0
for profit in firmsProfit.values():
    if profit > 0:
        firmsWithProfit += 1
        averageProfit += profit
statData = [firmsProfit, {"average_profit": averageProfit/firmsWithProfit}]


with open('res5.7.json', 'w', encoding='utf-8') as resFile:
    json.dump(statData, resFile, ensure_ascii=False)
    resFile.close()
