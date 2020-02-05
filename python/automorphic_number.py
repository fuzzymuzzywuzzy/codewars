#https://www.codewars.com/kata/5a58d889880385c2f40000aa/train/python

def automorphic(n):
    digits = [int(x) for x in str(n)]
    squared = n**2
    squared_digits = [int(x) for x in str(squared)]

    if squared_digits[len(squared_digits)-len(digits):len(squared_digits)] == digits:
        return True

    else:
        return False