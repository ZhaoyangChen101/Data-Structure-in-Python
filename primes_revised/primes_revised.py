# -*- coding: utf-8 -*-
# Nimi: Zhaoyang Chen
# Opiskelijanumero: 875497
# ​‌​​​​​‌‌‌​‌​​​ Implement the nof_primes_revised function here below
import math


def check_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True


def nof_primes_revised(li: list):
    """ Return the number of prime numbers in a list """
    counter = 0
    prime_set = {2, 3}
    composite_set = {4, 6}
    for n in li:
        if n in prime_set:
            counter += 1
        elif n in composite_set:
            continue
        else:
            is_prime = check_prime(n)
            if is_prime:
                counter += 1
                prime_set.add(n)
            else:
                composite_set.add(n)
    return counter
