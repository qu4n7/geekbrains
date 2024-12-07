# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве
# медиану. Медианой называется элемент ряда, делящий его на две равные части: в одной находятся 
# элементы, которые не меньше медианы, в другой – не больше медианы. Задачу можно решить без 
# сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, 
# который не рассматривался на уроках

import numpy as np

spam_inp = int(input('задайте длину массива: '))
array = np.random.randint(0, 49, size = spam_inp)
print(f'исходный массив:\n {array}')

def gnome_sort(array):
    i = 1
    while i < len(array):
        if not i or array[i - 1] <= array[i]:
            i += 1
        else:
            array[i], array[i - 1] = array[i - 1], array[i]
            i -= 1
    return array

def median(array):
    gnome_sort(array)
    length = len(array)
    if length % 2 != 0: 
        midle = (length // 2)
        result = array[midle]
    else:
        odd = (length // 2) - 1
        even = (length // 2) 
        result = float(array[odd] + array[even]) // 2
    return result

median(array)