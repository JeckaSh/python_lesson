# Задание 5

# Напишите функцию print_digit_sum(), которая принимает одно натуральное число num и выводит на печать сумму его цифр.

'''
# объявление функции
def print_digit_sum(num):
    pass

# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)
'''

def print_digit_sum(num):
    s = str(num)

    s_list = list(s)
    
    for num in range(len(s_list)):
        s_list[num] = int(s_list[num])

    print(sum(s_list))

n = int(input())

print_digit_sum(n)