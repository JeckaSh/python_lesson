# Задание 7

# Панграмма – это фраза, содержащая в себе все буквы алфавита. Обычно панграммы используют для презентации шрифтов, чтобы можно было в одной фразе рассмотреть все глифы.

# Напишите функцию is_pangram(text), которая принимает в качестве аргумента строку текста на английском языке и возвращает значение True, если текст является панграммой, или False в противном случае.

# Примечание 1. Гарантируется, что введённая строка содержит только буквы английского алфавита и пробелы.

# Примечание 2. Приведённый ниже код:

# print(is_pangram('Jackdaws love my big sphinx of quartz'))
# print(is_pangram('The jay pig fox zebra and my wolves quack'))
# print(is_pangram('Hello world'))
                  
# должен выводить:

# True
# True
# False

def is_pangram(text):
    abc = "abcdefghijklmnopqrstuvwxyz"

    for symbol in range(len(abc)):
        if abc[symbol] not in text.lower():
            return False
        
    return True
        

text = input()

print(is_pangram(text))