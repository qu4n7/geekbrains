# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными 
# числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import numpy as np

spam_inp = int(input('задайте длину массива: '))
array = np.random.randint(0, 49, size = spam_inp)
print(f'исходный массив:\n {array}')

def merge(left, right):
    result=[] 
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        #print(result, '\n')
    result.extend(left[i:]) # чтобы добавить только элемент, а не весь список
    result.extend(right[j:]) # -//-
    return result

def merge_sort(array):
    # если длина массива 0 или 1, то он отсортирован
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left_subarray = merge_sort(array[:middle])
    right_subarray = merge_sort(array[middle:])
    return merge(left_subarray, right_subarray)
    print(merge_sort(array))

print(merge_sort(array))