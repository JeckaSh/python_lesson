# Задание 14

# Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и возвращающую список всех делителей данного числа в порядке возрастания.

# Примечание. Приведённый ниже код:

# print(get_factors(1))
# print(get_factors(5))
# print(get_factors(10))
                 
# должен выводить:

# [1]
# [1, 5]
# [1, 2, 5, 10]

'''
# объявление функции
def get_factors(num):
    pass

# считываем данные
n = int(input())

# вызываем функцию
print(get_factors(n))
'''

def get_factors(num):
    factors = []

    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    return factors


n = int(input())

print(get_factors(n))