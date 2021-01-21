"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, --- 3
заданный случайными числами на промежутке [-100; 100). ---- 1
Выведите на экран исходный и отсортированный массивы. ---- 2
Сортировка должна быть реализована в виде функции. ---- 3
Обязательно доработайте алгоритм (сделайте его умнее). ---- 4
Идея доработки: если за проход по списку не совершается ни одной сортировки, то завершение
Обязательно сделайте замеры времени обеих реализаций --- 5

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""

from random import randint
from timeit import timeit


# 3 зададим функцию для сортировки нашего массива методом "пузырька"
def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


# Постараемся доработать фунцию ---- 4
def bubble_sort_opt(lst_obj):
    n = 1
    m = 0  # введем еще один счетчик присвоив ему значение ноль
    while n < len(lst_obj):
        p = m
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
                m += 1
                """
                если на очередной итерации произойдет сортировка тогда прибавляем 1 к переменной m
                тогда m != p продолжаем цикл
                если на очередной итерации не произойдет ни одной сортировки, значит список уже отсортирован,
                тогда значение m останется без изменений и получится m == p, значит прерываем цикл
                """
        if m == p:
            break
        else:
            n += 1
    return lst_obj


# 1 зададим случайный массив на промежутке от -100 до 100
origin_list = [randint(-100, 1000) for i in range(1000)]
# 2 выведем его на экран
print(f'Исходный список {origin_list}')
# выведем на экран отсортированный список ---- 2
print(f'Список отсортированный функцией без доработки {bubble_sort(origin_list[:])}')
print(f'Список отсартированный функцией с доработкой {bubble_sort_opt(origin_list[:])}')

# сделаем замеры ---- 5
print('Время функции без доработки', end=': ')
print(timeit("bubble_sort(origin_list[:])", setup="from __main__ import bubble_sort, origin_list", number=1000))
print('Время функции с доработкой', end=': ')
print(timeit("bubble_sort_opt(origin_list[:])", setup="from __main__ import bubble_sort_opt, origin_list",
             number=1000))

"""
Результат для массива из 10 элементов:
Исходный список [93, -40, -81, 84, -53, -38, 70, 66, 9, -44]
Список отсортированный функцией без доработки [93, 84, 70, 66, 9, -38, -40, -44, -53, -81]
Список отсартированный функцией с доработкой [93, 84, 70, 66, 9, -38, -40, -44, -53, -81]
Время функции без доработки: 0.010961699999999998
Время функции с доработкой: 0.0090593

Результат для массива из 100 элементов:
Время функции без доработки: 0.7553436
Время функции с доработкой: 0.9691068

Результат для массива из 1000 элементов:
Время функции без доработки: 85.9414752
Время функции с доработкой: 97.7912505

Вариант с доработкой выполняется дольше в большенстве случаев.
Если же исходный список будет отсортирован в значительной свой части,
то благодаря доработке можно получить выйгрыш по времени.
Однако получить такой список случайным образом крайне трудно.
В одном случае из десяти удалось получить следующий результат для массива из 1000 элементов:
Время функции без доработки: 85.8807119
Время функции с доработкой: 81.64485110000001
"""


def bubble_sort3(lst_obj):
    n = 1
    while n < len(lst_obj) // 2:
        for i in range(len(lst_obj)-n):
            if lst_obj[i] < lst_obj[i+1]:
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
        n += 1
    return lst_obj


origin_list2 = bubble_sort3(origin_list[:])
print(origin_list2)
print('Время сортировки частично отсортированного массива функции без доработки', end=': ')
print(timeit("bubble_sort(origin_list2[:])", setup="from __main__ import bubble_sort, origin_list2", number=1000))
print('Время сортировки частично отсортированного массива функции с доработкой', end=': ')
print(timeit("bubble_sort_opt(origin_list2[:])", setup="from __main__ import bubble_sort_opt, origin_list2",
             number=1000))


"""
Как видим в случае частично отсортированного массива получается получить прибавку по времени:

Время сортировки частично отсортированного массива функции без доработки: 31.88411500000001
Время сортировки частично отсортированного массива функции с доработкой: 26.0403886
"""