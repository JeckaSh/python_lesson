# Задание 44

# Под "тяжестью" слова будем понимать сумму кодов по таблице Unicode всех символов этого слова. Напишите программу, которая принимает 4 слова и находит среди них самое тяжёлое слово. Если самых тяжёлых слов будет несколько, то программа должна вывести первое из них.

# Формат входных данных
# На вход программе подаются 4 слова, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести самое тяжёлое слово в строке.

sum_dict = {}
max_heavy = 0

for i in range(4):
    sum = 0
    word = input()
    for j in range(len(word)):
        sum += ord(word[j])
    
    sum_dict[word] = sum

    if sum > max_heavy:
        max_heavy = sum

heavy = max(sum_dict.values())

for key, value in sum_dict.items():
    if value == max_heavy:
        print(key)
        break
