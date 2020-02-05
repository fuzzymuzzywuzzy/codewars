#https://www.codewars.com/kata/5738f5ea9545204cec000155/train/python

def count_letters_and_digits(s):

    letters = sum(x.isalpha() for x in s)
    digits = sum(x.isdigit() for x in s)

    return letters+digits