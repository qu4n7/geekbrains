# Задача 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# с функциями min(), max()

import random
import cProfile
def min_max_func(size):
    min_item, max_item = 0, 100
    array = [random.randint(min_item, max_item) for _ in range(size)]
    print(array)

    minim_ = min(array)
    maxim_ = max(array)

    pos_min = array.index(minim_)
    pos_max = array.index(maxim_)

    print(f'индекс минимума: {pos_min}, индекс максимума {pos_max}')
    array[pos_min], array[pos_max] = array[pos_max], array[pos_min]
    print(array)

# замеряю алгоритм через Δ размера массива
# timeit:
     
# 200 loops, best of 5: 196 usec per loop - 10
# 200 loops, best of 5: 203 usec per loop - 10
# 200 loops, best of 5: 202 usec per loop - 10

# 200 loops, best of 5: 279 usec per loop - 50
# 200 loops, best of 5: 271 usec per loop - 50
# 200 loops, best of 5: 278 usec per loop - 50

# 200 loops, best of 5: 390 usec per loop - 100
# 200 loops, best of 5: 355 usec per loop - 100
# 200 loops, best of 5: 374 usec per loop - 100

# 200 loops, best of 5: 829 usec per loop - 300
# 200 loops, best of 5: 848 usec per loop - 300
# 200 loops, best of 5: 827 usec per loop - 300

# теперь - через cProfile: 

cProfile.run('min_max_func(10)')
# 1    0.000    0.000    0.001    0.001 task_4_2.py:7(min_max_func) - 10
# 1    0.000    0.000    0.001    0.001 task_4_2.py:7(min_max_func) - 50
# 1    0.000    0.000    0.006    0.006 task_4_1.py:4(min_max_iter) - 100
# 1    0.000    0.000    0.002    0.002 task_4_2.py:7(min_max_func) - 300