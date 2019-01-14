# здесь я вывел в график результаты оценки:

import matplotlib.pyplot as plt
import pandas as pd

def aver(l):
    return sum(l) / len(l)

iter10, iter50, iter100, iter300  = [198, 204, 207], [297, 283, 294], [389, 415, 394], [877, 979, 986]
func10, func50, func100, func300  = [196, 203, 202], [279, 271, 278], [390, 355, 374], [829, 848, 827]

x = [10, 50, 100, 300]
y_iter = [aver(iter10), aver(iter50), aver(iter100), aver(iter300)]
y_func = [aver(func10), aver(func50), aver(func100), aver(func300)]
plt.plot(x, y_iter, color = 'olive', linewidth = 2)
plt.plot(x, y_func, color = 'red', linewidth = 2)

# предполагаю, что алгоритмы имеют сложность O(n), алгоритм с фукнциями min(), max() предпочтительнее
# хотя я не понял, почему cProfile на первом алгоримте выдавал 1 итерацию.