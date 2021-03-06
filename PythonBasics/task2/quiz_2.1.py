"""
Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""
import sys


typedArray = [1, 2, 3, 4]
dict = {"a": 1, "b": 2, "h": hex(10)}

mixedArray = ["1", 1, "2", 3, typedArray, dict, hex, sys]
for a in mixedArray:
    print(type(a))
