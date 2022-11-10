def shift_selection_to_right(a, beg, end):
    for i in range(end, beg, -1):
        a[i] = a[i - 1]


def merge_sort_in_place(a, beg, end):
    # Implement this function without creating any new data structures
    # pass
    if (beg + 1) == end:  # base case
        return
    else:
        mid = (beg + end) // 2
        # left_list = a[beg:mid]
        # right_list = a[mid:end]
        merge_sort_in_place(a, beg, mid)
        merge_sort_in_place(a, mid, end)
        # conquer: merge and order the two parts
        left = beg
        right = mid
        while left != right and right != end:
            if a[left] <= a[right]:
                left += 1
            else:
                temp = a[right]
                shift_selection_to_right(a, left, right)
                a[left] = temp
                left += 1
                right += 1

def check(input, expected):
    print('Sorting: ' + str(input))
    merge_sort_in_place(input, 0, len(input))
    print('Result: ' + str(input) + '\n')
    return input == expected


if (
        check([4, 7, 4, 1], [1, 4, 4, 7])
        and check([1, 2, 3, 9, 8], [1, 2, 3, 8, 9])
        and check([1], [1])
):
    print('Tests pass! Next, submit your code to A+')
else:
    print('A test failed. Fix your program.')
