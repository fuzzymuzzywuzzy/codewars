#https://www.codewars.com/kata/513e08acc600c94f01000001/train/python

def rgb(r,g,b):

    decimal_rgb = [r,g,b]

    for i, n in enumerate(decimal_rgb):
        if n < 0:
            decimal_rgb[i] = 0
        elif n > 255:
            decimal_rgb[i] = 255

    hexa_rgb = []
    output = ""

    decimal_to_hexa = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9,
               10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

    for n in decimal_rgb:
        first = int((n - n%16)/16)
        second = int((n/16 - first)*16)

        if first == 0:
            hexa_rgb.append(0)
            hexa_rgb.append(second)
        else:
            hexa_rgb.append(first)
            hexa_rgb.append(second)

    for i, n in enumerate(hexa_rgb):
        output += str(decimal_to_hexa[n])

    return output