"""
Выполнить функцию, которая принимает несколько параметров,
описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой.
"""


def userInfo(firstname, lastname, year, city, email, phone):
    print(f'имя: {firstname}, фамилия: {lastname}, год рождения: {year}, город проживания: {city}, email: {email}, телефон: {phone}')


userInfo(
    firstname="Иван",
    lastname="Иванов",
    year=2222,
    city="Racoon",
    email="ivan@umbrella.com",
    phone=88899900001
    )
