# -*- coding: utf-8 -*-
# Nimi: Zhaoyang Chen
# Opiskelijanumero: 875497
# ​‌​​​​​‌‌‌​‌​​​ Implement the sieve_of_eratosthenes function here below
import math


def sieve_of_eratosthenes(n):
    """ Return the number of prime numbers between the range (2, n) """
    if (n < 2):
        return 0
    else:
        A = list(range(n + 1))
        for i in range(2, int(math.sqrt(n + 1)) + 1):
            if A[i] != 0:
                j = i * i
                while j <= n + 1:
                    A[j] = 0
                    j += i
        p = 0
        for i in range(2, n + 1):
            if A[i] != 0:
                A[p] = A[i]
                p += 1
        return len(A[:p])

    # raise NotImplementedError("sieve_of_eratosthenes function is missing!") #Remove this line


# ​‌​​​​​‌‌‌​‌​​​ Driver program
def main():
    n = 10
    nof_primes = sieve_of_eratosthenes(n)
    print("The number of primes between the range (2, {:d}) is: {:d}"
          .format(n, nof_primes))


if __name__ == "__main__":
    main()
