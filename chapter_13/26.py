# Задание 26

# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое число, большее числа num.

# Примечание 1. Используйте функцию is_prime() из предыдущей задачи.

# Примечание 2. Приведённый ниже код:

# print(get_next_prime(6))
# print(get_next_prime(7))
# print(get_next_prime(14))
                  
# должен выводить:
 
# 7
# 11
# 17

'''
# объявление функции
def get_next_prime(num):
    pass

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
'''

# функция из прошлой задачи
def is_prime(num):
    factors = []

    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)

    if len(factors) == 2 and (1 in factors and num in factors):
        return True
    else:
        return False

def get_next_prime(num):
    canditate = num + 1

    while not is_prime(canditate):
        canditate += 1
    else:
        return canditate

n = int(input())

print(get_next_prime(n))