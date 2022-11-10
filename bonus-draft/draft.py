import timeit


def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)


def iterative_factorial(n):
    product = 1
    for i in range(n):
        product = product * (i + 1)
    return product


if __name__ == '__main__':
    start_time_iterative = timeit.default_timer()
    iterative_factorial(100)
    print(timeit.default_timer() - start_time_iterative)

    start_time_recursive = timeit.default_timer()
    recursive_factorial(100)
    print(timeit.default_timer() - start_time_recursive)
