# Задание 15

# Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую количество делителей данного числа.

# Примечание 1. Используйте уже реализованную функцию get_factors(num) из предыдущей задачи.

# Примечание 2. Приведённый ниже код:

# print(number_of_factors(1))
# print(number_of_factors(5))
# print(number_of_factors(10))
                  
# должен выводить:

# 1
# 2
# 4

def number_of_factors(num):
    factors = []

    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    return factors

n = int(input())

print(len(number_of_factors(n)))