# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный 
# случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный 
# массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм 
# (сделайте его умнее).

import numpy as np

spam_inp = int(input('задайте длину массива: '))
array = np.random.randint(-100, 99, size = spam_inp)
print(array)

def buble_sort(array):
    n = 1
    while n < len(array):
        for i in range(len(array)- n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
        print(array)
buble_sort(array)