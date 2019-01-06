# Задача 4. Определить, какое число в массиве встречается чаще всего.

# вызов библиотеки
import random

# генерирую случайный массив
size = 10
min_item, max_item = 0, 100
array = [random.randint(min_item, max_item) for _ in range(size)]
print(array)

# ввожу переменную наиболее частого значения (начну с начала списка) и переменную счетчика
mode = array[0]
mode_freq = 1
# пошел сравнивать, начиная с первого элемента, с каждым последующим
for i in range(size - 1):
    freq = 1
    for j in range(i + 1, size):
        if array[i] == array[j]:
            freq += 1
    if freq > mode_freq:
        mode_freq = freq
        mode = array[i]
 
if mode_freq > 1:
    print(f'число {mode} встречается чаще всего, а именно {mode_freq} раз')
else:
    print('все числа уникальны')