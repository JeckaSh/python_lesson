# Задание 17

# Напишите функцию get_last_index(data, value), которая принимает на вход список data и некоторое значение value и возвращает индекс последнего вхождения данного значения в список или текст «ERROR!» (без кавычек), если искомое значение отсутствует в списке.

# Примечание 1. Если искомое значение встречается в списке только один раз, то нужно вернуть индекс этого вхождения.

# Примечание 2. Приведённый ниже код:

# print(get_last_index(['🦆', '🐝', '🐍', '🐍', '🐝'], '🐝'))
# print(get_last_index(['Ross', 'Joey', 'Mike'], 'Ross'))
# print(get_last_index(['синий', 'белый', 'фиолетовый'], 'красный'))
                  
# должен выводить:

# 4 
# 0
# ERROR!
                  
# Примечание 3. Обратите внимание на то, что для принятия данных на вход в программе используется функция eval(). На текущем этапе обучения не нужно разбираться в её устройстве: данная функция изучается подробно в нашем курсе для профессионалов.

'''
# объявление функции
def get_last_index(data, value):
    pass

# считываем данные
data = eval(input())
value = eval(input())

# вызываем функцию
print(get_last_index(data, value))
'''

def get_last_index(data, value):
    last_index = -1

    for i in range(len(data)):
        if data[i] == value:
            last_index = i

    if last_index == -1:
        return 'ERROR!'
    else:
        return last_index
            

data = eval(input())
value = eval(input())

print(get_last_index(data, value))