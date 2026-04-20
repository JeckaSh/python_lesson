# Задание 11

# Напишите функцию code_format(text), которая принимает строку текста text, оборачивает её в теги <code></code> и возвращает результат.

'''
# объявление функции
def code_format(text):
    pass

# считываем данные
text = input()

# вызываем функцию
print(code_format(text))
'''

def code_format(text):
    return f"<code>{text}</code>"

text = input()

print(code_format(text))