# -*- coding: utf-8 -*-
# Nimi: Zhaoyang Chen
# Opiskelijanumero: 875497
"""Return the sequence `lst` sorted in-place in ascending order."""


# ​‌​​​​​‌‌‌​‌​​​ Note: in-place means, that the method shouldn't create and return another
# ​‌​​​​​‌‌‌​‌​​​ list, but sort the same list object it received, and return it. It is
# ​‌​​​​​‌‌‌​‌​​​ allowed, however, to copy values to another list and use it to get the
# ​‌​​​​​‌‌‌​‌​​​ given list sorted. Note that this will take extra memory.

# ​‌​​​​​‌‌‌​‌​​​ The solution must be fast in order to complete the biggest sorting
# ​‌​​​​​‌‌‌​‌​​​ problems in time before the time runs out and the evaluator
# ​‌​​​​​‌‌‌​‌​​​ terminates the attempt.

# ​‌​​​​​‌‌‌​‌​​​ If you are implementing a recursive mergesort, remember to
# ​‌​​​​​‌‌‌​‌​​​ divide only up until a certain sublist size, eg. 20, and then sort
# ​‌​​​​​‌‌‌​‌​​​ the sublist with another method, eg. selection sort. Dividing and
# ​‌​​​​​‌‌‌​‌​​​ recursing up until sublists of size 1 is not effective!
# raise NotImplementedError('my_sort does not sort anything yet.')

def my_sort(lst):
    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        i = 0
        j = len(lst) - 1
        quicksort(lst, i, j)
        return lst


def quicksort(lst, i, j):
    pivotIndex = findpivot(lst, i, j)
    lst[j], lst[pivotIndex] = lst[pivotIndex], lst[j]
    k = partition(lst, i, j - 1, lst[j])
    lst[k], lst[j] = lst[j], lst[k]
    if (k - i) > 9:
        quicksort(lst, i, k - 1)
    else:
        insertionsort(lst, i, k - 1)
    if (j - k) > 9:
        quicksort(lst, k, j)
    else:
        insertionsort(lst, k, j)


def findpivot(list, start, end):
    temp = []
    temp.append(list[start])
    temp.append(list[end])
    temp.append(list[(start + end) // 2])
    insertionsort(temp, 0, 2)
    midindex = list.index(temp[1])
    return midindex


def partition(lst, left, right, pivot):
    while left <= right:
        while lst[left] < pivot:
            left += 1
        while right >= left and lst[right] >= pivot:
            right -= 1
        if right > left:
            lst[right], lst[left] = lst[left], lst[right]
    return left


def insertionsort(lst, start, end):
    for i in range(start, end + 1):
        j = i
        while j > start:
            if lst[j] < lst[j - 1]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
                j -= 1
            else:
                break
