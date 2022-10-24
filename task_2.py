'''задача 2 . Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
 исходной последовательности.'''

from random import randint

def random_list(start,end,size):
    rand_list = []
    for _ in range(size):
        rand_list.append(randint(start, end))
    return rand_list

list_num = random_list(1,20,30)
print()
print(f'Задана последовательность чисел: {list_num}')
print(f'Неповторяющиеся элементы: {set(list_num)}')

