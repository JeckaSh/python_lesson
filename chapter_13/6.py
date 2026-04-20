# Задание 6

# Напишите функцию print_sorted_hyphen(s), которая принимает строку s, состоящую из слов, разделённых дефисами, и выводит эти слова на одной строке в лексикографическом порядке, разделённые дефисами.

# Примечание. Гарантируется, что в последовательности будет более одного слова.

'''
# объявление функции
def print_sorted_hyphen(s):
    pass

# считываем данные
s = input()

# вызываем функцию
print_sorted_hyphen(s)
'''

def print_sorted_hyphen(s):
    list_s = s.split('-')
    sorted_list = sorted(list_s)

    print(*sorted_list, sep='-')

s = input()

print_sorted_hyphen(s)