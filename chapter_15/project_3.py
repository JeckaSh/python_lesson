# Проект 3

# Генератор безопасного пароля

# Описание проекта: программа генерирует заданное количество паролей и включает в себя умную настройку на длину пароля, а также на то, какие символы требуется в него включить, а какие исключить.

# Составляющие проекта:

# Целые числа (тип int);
# Переменные;
# Ввод / вывод данных (функции input() и print());
# Условный оператор (if/elif/else);
# Цикл for;
# Написание пользовательских функций;
# Работа с модулем random для генерации случайных чисел.

import random

digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_"

chars = ""

pass_count = int(input("Сколько паролей сгенерировать? "))
pass_len = int(input("Укажите длину пароля: "))
digits_include = input("Включать ли в пароль цифры (д/н)? ")
lowercase_letters_include = input("Включать ли прописные буквы в пароль (д/н)? ")
uppercase_letters_include = input("Включать ли строчные буквы в пароль (д/н)? ")
punctuation_include = input('Включать ли символы "!#$%&*+-=?@^_" в пароль (д/н)? ')
other_symbols_include = input("Исключать ли неоднозначные (il1Lo0O) символы (д/н)? ")


def generate_pass():
    avialable_chars = ""
    if digits_include.lower() == "д":
        avialable_chars += digits

    if lowercase_letters_include.lower() == "д":
        avialable_chars += lowercase_letters

    if uppercase_letters_include.lower() == "д":
        avialable_chars += uppercase_letters

    if punctuation_include.lower() == "д":
        avialable_chars += punctuation

    if other_symbols_include.lower() == "д":
        for c in "il1Lo0O":
            avialable_chars = avialable_chars.replace(c, "")

    password = "".join(random.choice(avialable_chars) for _ in range(pass_len))
    return password


for _ in range(pass_count):
    print(generate_pass())
