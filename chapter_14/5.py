# Задание 5

# Напишите функцию get_month(language, number), которая принимает на вход два аргумента language – язык ru или en и number – номер месяца (от 1 до 12 включительно) и возвращает название месяца на русском или английском языке.

# Примечание. Приведённый ниже код:

# print(get_month('ru', 1))
# print(get_month('ru', 12))
# print(get_month('en', 1))
# print(get_month('en', 10))

# должен выводить:

# январь
# декабрь
# january
# october

def get_month(language, number):
    ru = [
        "январь",
        "февраль",
        "март",
        "апрель",
        "май",
        "июнь",
        "июль",
        "август",
        "сентябрь",
        "октябрь",
        "ноябрь",
        "декабрь",
    ]
    en = [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december",
    ]

    if language == 'ru':
        return ru[number - 1]
    elif language == 'en':
        return en[number - 1]


lan = input()
num = int(input())

print(get_month(lan, num))
