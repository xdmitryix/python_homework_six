# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15




def progres_inp(number, step, quantity):
    print(number, end=' ')
    for i in range(1, quantity):
        number += step
        print(number, end=' ')


a = int(input('введи первое число арифметической прогрессии: '))
d = int(input('введи шаг арифметической прогрессии: '))
n = int(input('введи количество членов арифметической прогрессии: '))
progres_inp(a, d, n)
