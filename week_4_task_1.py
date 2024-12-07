# Задача 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# здесь без функций min(), max()

import random
import cProfile
def min_max_iter(size):
    min_item, max_item = 0, 100
    array = [random.randint(min_item, max_item) for _ in range(size)]
    print(array)

    minim, maxim = 0, 0

    for i in range(len(array)):
        if array[i] < array[minim]:
            minim = i
        elif array[i] > array[maxim]:
            maxim = i
    print(f'индекс минимума: {minim}, индекс максимума {maxim}')

    array_maxim_temp = array[maxim]
    array[maxim] = array[minim]
    array[minim] = array_maxim_temp
    print(array)

# замеряю алгоритм через Δ размера массива
# timeit:
     
# 200 loops, best of 5: 198 usec per loop - 10
# 200 loops, best of 5: 204 usec per loop - 10
# 200 loops, best of 5: 207 usec per loop - 10

# 200 loops, best of 5: 297 usec per loop - 50
# 200 loops, best of 5: 283 usec per loop - 50
# 200 loops, best of 5: 294 usec per loop - 50

# 200 loops, best of 5: 389 usec per loop - 100
# 200 loops, best of 5: 415 usec per loop - 100
# 200 loops, best of 5: 394 usec per loop - 100

# 200 loops, best of 5: 877 usec per loop - 300
# 200 loops, best of 5: 979 usec per loop - 300
# 200 loops, best of 5: 986 usec per loop - 300

# теперь с умным видом замеряю через cProfile, типа я понимаю, зачем это нужно было: 

cProfile.run('min_max_iter(300)')
# 1    0.000    0.000    0.005    0.005 task_4_1.py:4(min_max_iter) - 10
# 1    0.000    0.000    0.006    0.006 task_4_1.py:4(min_max_iter) - 50
# 1    0.000    0.000    0.006    0.006 task_4_1.py:4(min_max_iter) - 100
# 1    0.000    0.000    0.006    0.006 task_4_1.py:4(min_max_iter) - 300