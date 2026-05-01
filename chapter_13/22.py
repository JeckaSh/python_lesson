# Задание 22

# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и возвращает значение True, если указанный текст является палиндромом, или False в противном случае.

# Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях

# Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте пробелы и символы ,.!?-.

# Примечание 3. Приведённый ниже код:

# print(is_palindrome('А роза упала на лапу Азора.'))
# print(is_palindrome('Gabler Ruby - burrel bag!'))
# print(is_palindrome('BEEGEEK'))

# должен выводить:

# True
# True
# False

'''
# объявление функции
def is_palindrome(text):
    pass

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
'''

def is_palindrome(text):
    text = text.replace(' ', '')
    text = text.replace('-', '')
    text = text.replace(',', '')
    text = text.replace('.', '')
    text = text.replace('?', '')
    text = text.replace('!', '')

    if text.lower() == text[::-1].lower():
        return True
    else:
        return False

txt = input()

print(is_palindrome(txt))

'''
Решение от кураторов

# объявление функции
def is_palindrome(text):
    symbols = [' ', ',', '.', '!', '?', '-']
    for c in symbols:
        text = text.replace(c, '')
    text = text.lower()
    return text == text[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))
'''