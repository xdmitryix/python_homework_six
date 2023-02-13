# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]


def min_max(arr_num, min_num, max_num):
    arr_result = []
    for i in range(0, len(arr_num)):
        if arr_num[i] <= max_num and arr_num[i] >= min_num:
            arr_result.append(i)
    print(arr_result)


numbers = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min = int(input('введи минимальное число диапазона: '))
max = int(input('введи аксимальное число диапазона: '))
print(numbers)
min_max(numbers, min, max)

