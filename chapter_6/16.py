# Задание 16

# Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое длинное название города.

# Формат входных данных
# На вход программе подаются названия трёх городов, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести самое короткое и длинное название города, каждое на отдельной строке.

# Примечание. Гарантируется, что длины названий всех трёх городов различны.

city1 = input()
city2 = input()
city3 = input()

c1_dist = len(city1)
c2_dist = len(city2)
c3_dist = len(city3)

# short city
if c1_dist < c2_dist and c1_dist < c3_dist:
    print(city1)
elif c2_dist < c1_dist and c2_dist < c3_dist:
    print(city2)
elif c3_dist < c2_dist and c3_dist < c1_dist:
    print(city3)

# long city
if c1_dist > c2_dist and c1_dist > c3_dist:
    print(city1)
elif c2_dist > c1_dist and c2_dist > c3_dist:
    print(city2)
elif c3_dist > c2_dist and c3_dist > c1_dist:
    print(city3)