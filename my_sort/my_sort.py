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
    elif len(lst) <= 10:
        insertionsort(lst, 0, len(lst) - 1)
        return lst
    else:
        dict = {}
        for num in lst:
            if num in dict.keys():
                dict[num] += 1
            else:
                dict[num] = 1
            # for value in dict.values():
            #     if value > 20:
            #         return radixsort(dict)
        if len(dict) < len(lst) / 2:
            return radixsort(dict)
        i = 0
        j = len(lst) - 1
        quicksort(lst, i, j)
        return lst


def radixsort(dict):
    nums = list(dict.keys())
    insertionsort(nums, 0, len(nums) - 1)
    temp = []
    #dict[nums[0]] -= 1
    # for i in range(1, len(nums)):
    #     dict[nums[i]] = dict[nums[i - 1]] + dict[nums[i]]
    for num in nums:
        while dict[num] != 0:
            temp.append(num)
            dict[num] -= 1
    return temp


def quicksort(lst, i, j):
    pivotIndex = findpivot(lst, i, j)
    lst[j], lst[pivotIndex] = lst[pivotIndex], lst[j]
    k = partition(lst, i, j - 1, lst[j])
    lst[k], lst[j] = lst[j], lst[k]
    if (k - i) > 10:
        quicksort(lst, i, k - 1)
    else:
        insertionsort(lst, i, k - 1)
    if (j - k) > 10:
        quicksort(lst, k, j)
    else:
        insertionsort(lst, k, j)


def findpivot(list, start, end):
    # temp = []
    # temp.append(list[start])
    # temp.append(list[end])
    # temp.append(list[(start + end) // 2])
    # insertionsort(temp, 0, 2)
    # midindex = list.index(temp[1])
    # return midindex
    return (start + end) // 2


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
