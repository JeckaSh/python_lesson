# Задание 6

# Дано натуральное число. Напишите программу, которая вычисляет:

# количество цифр 3 в нём;
# сколько раз в нём встречается последняя цифра;
# количество чётных цифр;
# сумму его цифр, больших пяти;
# произведение цифр, больших семи (если цифр больших семи нет, то вывести 1, если такая цифра одна, то вывести её);
# сколько раз в нём встречаются цифры 0 и 5 (всего суммарно).

# Формат входных данных 
# На вход программе подаётся одно натуральное число.

# Формат выходных данных
# Программа должна вывести значения указанных величин в указанном порядке, каждую на отдельной строке.

num = int(input())

last_digit = 0

first_last_digit = num % 10

three_count = 0
last_digit_count = 0
event_count = 0
sum_of_more_than_five = 0
multi_of_more_than_seven = 1
zero_and_five_in_num_count = 0

while num != 0:
    last_digit = num % 10

    if last_digit == 3:
        three_count +=1

    if last_digit == first_last_digit:
        last_digit_count +=1

    if last_digit % 2 == 0:
        event_count +=1

    if last_digit > 5:
        sum_of_more_than_five += last_digit

    if last_digit > 7:
        multi_of_more_than_seven *= last_digit

    if (last_digit == 0) or (last_digit == 5):
        zero_and_five_in_num_count +=1

    num //= 10

print(three_count)
print(last_digit_count)
print(event_count)
print(sum_of_more_than_five)
print(multi_of_more_than_seven)
print(zero_and_five_in_num_count)
    
