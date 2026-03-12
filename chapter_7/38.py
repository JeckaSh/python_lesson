# Задание 38

# Дано натуральное число. Напишите программу, которая вычисляет:

# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

# Формат входных данных
# На вход программе подаётся натуральное число.

num = int(input())
n = len(str(num))

sum = 0  # сумма всех чисел
n_count = 0  # количество чисел
n_multi = 1  # произведение чисел
n_average = 0  # среднее арифметическое чисел

num_copy = num  # копия для дальнейших расчетов

for i in range(1, n + 1):
    digit = num // 10 ** (n - i) % 10
    sum += digit
    n_count += 1
    n_multi *= digit

n_average = sum / n_count

n_first_digit = num_copy // 10 ** (n_count - 1)  # первая цифра числа
n_last_digit = num_copy // 10 ** (n - n_count) % 10  # последняя цифра числа

sum_first_last_digit = (
    n_first_digit + n_last_digit
)  # сумма первой и последней цифр числа

print(sum)
print(n_count)
print(n_multi)
print(n_average)
print(n_first_digit)
print(sum_first_last_digit)
