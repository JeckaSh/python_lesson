# Задание 18

# На вход программе подаётся одна строка. Напишите программу, которая выводит:

# общее количество символов в строке;
# исходную строку, повторённую 3 раза;
# первый символ строки;
# первые три символа строки;
# последние три символа строки;
# строку в обратном порядке;
# строку с удалённым первым и последним символами.

# Формат входных данных
# На вход программе подаётся одна строка, длина которой больше 3 символов.

# Формат выходных данных
# Программа должна вывести данные в соответствии с условием. Каждое значение выводится на отдельной строке.

word = input()

word_len = len(word)
triple_world = word * 3
first_symbol = word[:1]
from_first_to_three_symbols = word[:3]
mirror_from_first_to_three_symbols = word[-3:]
mirror_word = word[::-1]
delete_symbols = word[1:-1]

print(word_len)
print(triple_world)
print(first_symbol)
print(from_first_to_three_symbols)
print(mirror_from_first_to_three_symbols)
print(mirror_word)
print(delete_symbols)