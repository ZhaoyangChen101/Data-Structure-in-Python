# -*- coding: utf-8 -*-
# Nimi: Zhaoyang Chen
# Opiskelijanumero: 875497
# ​‌​​​​​‌‌‌​‌​​​ Implement the generate_image and fract functions here below

from minipng import Image
import math


# ​‌​​​​​‌‌‌​‌​​​ Complete this function
def fract(img, x1, y1, x2, y2, c):
    # pass
    width = (x2 - x1 + 1) // 3
    counter = math.log(width, 3)
    if counter == 0:
        return 0
    elif counter == 1:
        img.rectangle(x1 + width, y2 - 2 * width + 1, x1 + 2 * width - 1, y2 - width, c)
        return 9
    else:
        img.rectangle(x1 + width, y2 - 2 * width + 1, x1 + 2 * width - 1, y2 - width, c)
        # since y1 is never used in the calculation of positions, it is used to alternate between 7 and 5 recursions.
        if y1 == 0:  # 7 iterations
            # fract(img, x1 - 2 * width, y1 - 2 * width, x1 - width - 1, y1 - width - 1, c)
            # fract(img, x1 + width, y1 - 2 * width, x1 + 2 * width - 1, y1 - width - 1, c)
            # fract(img, x2 + width, y1 - 2 * width, x2 + 2 * width - 1, y1 - width - 1, c)
            # fract(img, x1 - 2 * width, y1 + width, x1 - width - 1, y1 + 2 * width - 1, c)
            # fract(img, x1 - 2 * width, y2 + width, x1 - width - 1, y2 + 2 * width - 1, c)
            # fract(img, x1 + width, y2 + width, x1 + 2 * width - 1, y2 + 2 * width - 1, c)
            # fract(img, x2 + width, y2 + width, x2 + 2 * width - 1, y2 + 2 * width - 1, c)

            # fract(img, x1, y1, x1 + width - 1, y1 + width - 1, c)
            # fract(img, x1 + width, y1, x1 + 2 * width - 1, y1 + width - 1, c)
            # fract(img, x1 + 2 * width, y1, x1 + 3 * width - 1, y1 + width - 1, c)
            # fract(img, x1, y1 + width, x1 + width - 1, y1 + 2 * width - 1, c)
            # fract(img, x1, y1 + 2 * width, x1 + width - 1, y1 + 3 * width - 1, c)
            # fract(img, x1 + width, y1 + 2 * width, x1 + 2 * width - 1, y1 + 3 * width - 1, c)
            # fract(img, x1 + 2 * width, y1 + 2 * width, x1 + 3 * width - 1, y1 + 3 * width - 1, c)

            # fract(img, x1, y2 - 3 * width + 1, x1 + width - 1, y2 - 2 * width, c)
            # fract(img, x1 + width, y2 - 3 * width + 1, x1 + 2 * width - 1, y2 - 2 * width, c)
            # fract(img, x1 + 2 * width, y2 - 3 * width + 1, x1 + 3 * width - 1, y2 - 2 * width, c)
            # fract(img, x1, y2 - 2 * width + 1, x1 + width - 1, y2 - width, c)
            # fract(img, x1, y2 - width + 1, x1 + width - 1, y2, c)
            # fract(img, x1 + width, y2 - width + 1, x1 + 2 * width - 1, y2, c)
            # fract(img, x1 + 2 * width, y2 - width + 1, x1 + 3 * width - 1, y2, c)
            y1 = 1
            # fract(img, x1, y1, x1 + width - 1, y2 - 2 * width, c)
            # fract(img, x1 + width, y1, x1 + 2 * width - 1, y2 - 2 * width, c)
            # fract(img, x1 + 2 * width, y1, x1 + 3 * width - 1, y2 - 2 * width, c)
            # fract(img, x1, y1, x1 + width - 1, y2 - width, c)
            # fract(img, x1, y1, x1 + width - 1, y2, c)
            # fract(img, x1 + width, y1, x1 + 2 * width - 1, y2, c)
            # fract(img, x1 + 2 * width, y1, x1 + 3 * width - 1, y2, c)
            return width * width + fract(img, x1, y1, x1 + width - 1, y2 - 2 * width, c) \
                   + fract(img, x1 + width, y1, x1 + 2 * width - 1, y2 - 2 * width, c) \
                   + fract(img, x1 + 2 * width, y1, x1 + 3 * width - 1, y2 - 2 * width, c) \
                   + fract(img, x1, y1, x1 + width - 1, y2 - width, c) \
                   + fract(img, x1, y1, x1 + width - 1, y2, c) \
                   + fract(img, x1 + width, y1, x1 + 2 * width - 1, y2, c) \
                   + fract(img, x1 + 2 * width, y1, x1 + 3 * width - 1, y2, c)

        if y1 == 1:  # 5 iterations
            # fract(img, x1 - 2 * width, y1 - 2 * width, x1 - width - 1, y1 - width - 1, c)
            # fract(img, x1 + width, y1 - 2 * width, x1 + 2 * width - 1, y1 - width - 1, c)
            # fract(img, x2 + width, y1 - 2 * width, x2 + 2 * width - 1, y1 - width - 1, c)
            # fract(img, x1 - 2 * width, y1 + width, x1 - width - 1, y1 + 2 * width - 1, c)
            # fract(img, x1 - 2 * width, y2 + width, x1 - width - 1, y2 + 2 * width - 1, c)

            # fract(img, x1 // 3 - 2 * width, y1 // 3 - 2 * width, x1 // 3 - width - 1, y1 // 3 - width - 1, c)
            # fract(img, x1 // 3 + width, y1 // 3 - 2 * width, x1 // 3 + 2 * width - 1, y1 // 3 - width - 1, c)
            # fract(img, x1 // 3 + initial_width - 1 + width, y1 - 2 * width, x1 // 3 + initial_width - 1 + 2 * width - 1,
            #       y1 - width - 1, c)
            # fract(img, x1 // 3 - 2 * width, y1 // 3 + width, x1 // 3 - width - 1, y1 // 3 + 2 * width - 1, c)
            # fract(img, x1 // 3 - 2 * width, y1 // 3 + initial_width - 1 + width, x1 // 3 - width - 1,
            #       y1 // 3 + initial_width - 1 + 2 * width - 1, c)
            # fract(img, x1 // 3 + width, y1 // 3 + initial_width - 1 + width, x1 // 3 + 2 * width - 1,
            #       y1 // 3 + initial_width - 1 + 2 * width - 1, c)
            # fract(img, x1 // 3 + initial_width - 1 + width, y1 // 3 + initial_width - 1 + width,
            #       x1 // 3 + initial_width - 1 + 2 * width - 1, y2 + 2 * width - 1, c)

            # fract(img, x1, y1, x1 + width - 1, y1 + width - 1, c)
            # fract(img, x1 + width, y1, x1 + 2 * width - 1, y1 + width - 1, c)
            # fract(img, x1 + 2 * width, y1, x1 + 3 * width - 1, y1 + width - 1, c)
            # fract(img, x1, y1 + width, x1 + width - 1, y1 + 2 * width - 1, c)
            # fract(img, x1, y1 + 2 * width, x1 + width - 1, y1 + 3 * width - 1, c)

            # fract(img, x1, y2 - 3 * width + 1, x1 + width - 1, y2 - 2 * width, c)
            # fract(img, x1 + width, y2 - 3 * width + 1, x1 + 2 * width - 1, y2 - 2 * width, c)
            # fract(img, x1 + 2 * width, y2 - 3 * width + 1, x1 + 3 * width - 1, y2 - 2 * width, c)
            # fract(img, x1, y2 - 2 * width + 1, x1 + width - 1, y2 - width, c)
            # fract(img, x1, y2 - width + 1, x1 + width - 1, y2, c)
            # fract(img, x1 + width, y2 - width + 1, x1 + 2 * width - 1, y2, c)
            # fract(img, x1 + 2 * width, y2 - width + 1, x1 + 3 * width - 1, y2, c)
            y1 = 0
            # fract(img, x1, y1, x1 + width - 1, y2 - 2 * width, c)
            # fract(img, x1 + width, y1, x1 + 2 * width - 1, y2 - 2 * width, c)
            # fract(img, x1 + 2 * width, y1, x1 + 3 * width - 1, y2 - 2 * width, c)
            # fract(img, x1, y1, x1 + width - 1, y2 - width, c)
            # fract(img, x1, y1, x1 + width - 1, y2, c)
            return width * width + fract(img, x1, y1, x1 + width - 1, y2 - 2 * width, c) + \
                   fract(img, x1 + width, y1, x1 + 2 * width - 1, y2 - 2 * width, c) + \
                   fract(img, x1 + 2 * width, y1, x1 + 3 * width - 1, y2 - 2 * width, c) + \
                   fract(img, x1, y1, x1 + width - 1, y2 - width, c) + \
                   fract(img, x1, y1, x1 + width - 1, y2, c)


# ​‌​​​​​‌‌‌​‌​​​ Helper function
def generate_image(level):
    # ​‌​​​​​‌‌‌​‌​​​ Initialize image and color
    w = 3 ** level
    img = Image(w, w)
    c = [0, 192, 128]

    # ​‌​​​​​‌‌‌​‌​​​ Example on how to draw a rectangle
    # d = w // 9
    # img.rectangle(d, 2 * d, 3 * d, 4 * d, c)
    # d = w // 3
    # img.rectangle(d, d, 2 * d - 1, 2 * d - 1, c)
    # ​‌​​​​​‌‌‌​‌​​​ Example ends
    # counter = level - 1
    # fract(img, d, d, 2 * d - 1, 2 * d - 1, c, counter)
    # ​‌​​​​​‌‌‌​‌​​​ Call fract(img, ...) here
    # ​‌​​​​​‌‌‌​‌​​​fract(img)
    num = fract(img, 0, 0, w - 1, w - 1, c)

    img.write_to_file('fractal2.png')
    return num


if __name__ == '__main__':
    # ​‌​​​​​‌‌‌​‌​​​ You can write your test code here
    # generate_image(5)
    print(generate_image(5))
