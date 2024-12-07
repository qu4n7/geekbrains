# Задача 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# вызов библиотеки
import random

# генерирую случайный массив
size = 10
min_item, max_item = 0, 100
array = [random.randint(min_item, max_item) for _ in range(size)]
print(array)

# т.к. запрещено применять max(), min(), начнем с вводна переменных под мак и мин
minim = 0
maxim = 0
for i in range(size):
    # ищем индекс мин
    if array[i] < array[minim]:
        minim = i
    # теперь индекс макс
    elif array[i] > array[maxim]:
        maxim = i
print(f'индекс минимума: {minim}, индекс максимума {maxim}')

# теперь меняем местами макс и мин, для чего выставскиваю в отдельную переменную один из экстремумов (макс)
array_maxim_temp = array[maxim]
array[maxim] = array[minim]
array[minim] = array_maxim_temp
print(array)