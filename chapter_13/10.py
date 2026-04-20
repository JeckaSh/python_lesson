# Задание 10

# Напишите функцию convert_to_miles(km), которая принимает в качестве аргумента расстояние в километрах и возвращает расстояние в милях. Формула для преобразования: мили = километры * 0.6214.

'''
# объявление функции
def convert_to_miles(km):
    pass

# считываем данные
num = int(input())

# вызываем функцию
print(convert_to_miles(num))
'''

def convert_to_miles(km):
    return km * 0.6214

num = int(input())

print(convert_to_miles(num))