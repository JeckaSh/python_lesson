# Задание 7

# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:

# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника;

# а затем выводит его.

# Примечание. Гарантируется, что основание треугольника – нечётное число.

'''
# объявление функции
def draw_triangle(fill, base):
    pass

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)
'''

def draw_triangle(fill, base):
    # вложенный цикл из 7.9 шаг 14
    for i in range(base):
        for j in range(i + 1):
            if j >= base - i:
                continue
            print(fill, end='')
        print()

fill = input()
base = int(input())

draw_triangle(fill, base)