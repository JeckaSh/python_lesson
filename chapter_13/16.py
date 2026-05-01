# Задание 16

# Напишите функцию get_unique(numbers), которая принимает список целых чисел numbers и возвращает новый список без повторяющихся значений, при этом сохраняя порядок появления чисел в исходном списке.

# Примечание 1. Приведённый ниже код:

# print(get_unique([1, 2, 4, 3, 4]))
# print(get_unique([0, -2, 1, -2, -3, 0]))
# print(get_unique([5, 6, 7]))
                 
# должен выводить:

# [1, 2, 4, 3]
# [0, -2, 1, -3]
# [5, 6, 7]
                  
# Примечание 2. Обратите внимание на то, что для принятия данных на вход в программе используется функция eval(). На текущем этапе обучения не нужно разбираться в её устройстве: данная функция изучается подробно в нашем курсе для профессионалов.

'''
# объявление функции
def get_unique(numbers):
    pass

# считываем данные
numbers = eval(input())

# вызываем функцию
print(get_unique(numbers))
'''

def get_unique(numbers):
    unique_numbers = []

    for item in numbers:
        if item not in unique_numbers:
            unique_numbers.append(item)

    return unique_numbers
        
numbers = eval(input())

print(get_unique(numbers))