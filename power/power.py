# -*- coding: utf-8 -*-
# Nimi: Zhaoyang Chen
# Opiskelijanumero: 875497

#​‌​​​​​‌‌‌​‌​​​ Implement the power function here below
#​‌​​​​​‌‌‌​‌​​​ You can expect to base and exponent to be 0 or greater.
#​‌​​​​​‌‌‌​‌​​​ Both of the paramaters are not allowed to be 0 at the same time

def power(base, exponent):
    #​‌​​​​​‌‌‌​‌​​​Write your code here
    #raise NotImplementedError("Fix me!")
    if exponent == 1:
        return base
    elif exponent == 0:
        return 1
    else:
        return base * power(base, exponent - 1)

def main():
    #​‌​​​​​‌‌‌​‌​​​Try your function
    base = 5
    exponent = 3
    print("{} ^ {} = {}".format(base, exponent, power(base, exponent)))

if __name__ == "__main__":
    main()

