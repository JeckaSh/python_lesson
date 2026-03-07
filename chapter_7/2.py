# Задание 2

# Напишите программу, которая использует ровно три цикла for для печати следующей последовательности символов:

'''
AAA
AAA
AAA
AAA
AAA
AAA
BBBB
BBBB
BBBB
BBBB
BBBB
E
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
G
'''
                  
# Формат входных данных
# На вход программе ничего не подаётся.

# Формат выходных данных
# Программа должна вывести указанную последовательность символов.

for i in range(6):
    print('AAA')

for j in range(5):
    print('BBBB')

print('E')

for k in range(9):
    print('TTTTT')

print('G')