#https://www.codewars.com/kata/5a87449ab1710171300000fd/train/python

def tidyNumber(n):
    digits = [int(x) for x in str(n)]
    digits_sorted = digits.copy()
    digits_sorted.sort()

    return True if (digits == digits_sorted) else False
