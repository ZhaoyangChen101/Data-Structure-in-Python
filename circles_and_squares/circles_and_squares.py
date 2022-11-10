# -*- coding: utf-8 -*-
# Nimi: Zhaoyang Chen
# Opiskelijanumero: 875497
#​‌​​​​​‌‌‌​‌​​​ Implement the count_circles_and_squares function here below

import math

def count_circles_and_squares(length, circles, squares):
    #​‌​​​​​‌‌‌​‌​​​ Write your code here
    #raise NotImplementedError("Fix me!")
    # if length < 1 and (squares == 0 or circles > squares):
    #     return 0, 0
    # elif length < 1 and squares >= circles:
    #     return 0, -1
    #
    # elif circles < squares:
    #     circles += 1
    #     length = length / math.sqrt(2)
    #     return circles + count_circles_and_squares(length, 0, 0)[0], squares + count_circles_and_squares(length, 0, 0)[1]
    # else:
    #     squares += 1
    #     circles += 1
    #     length = length / math.sqrt(2)
    #     return circles + count_circles_and_squares(length, 0, 0)[0], squares + count_circles_and_squares(length, 0, 0)[1]
    if length < 1:
        return circles, squares
    elif length >= 1 and circles == squares:
        circles += 1
        return count_circles_and_squares(length, circles, squares)
    elif length >= 1 and circles > squares:
        length = length / round(math.sqrt(2),6)
        length = round(length, 4)
        if length >= 1:
            squares += 1
            return count_circles_and_squares(length, circles, squares)
        else:
            return count_circles_and_squares(length, circles, squares)
#​‌​​​​​‌‌‌​‌​​​ A simple example
def main():
    length = 2
    circles, squares = count_circles_and_squares(length, 0, 0)
    print("Circles:", circles, "Squares:", squares)


if __name__ == "__main__":
    main()

