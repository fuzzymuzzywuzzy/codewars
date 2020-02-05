#https://www.codewars.com/kata/5a55f04be6be383a50000187/train/python

def special_number(number):
    special = list(range(0,6))
    num = [int(n) for n in str(number)]

    if [x for x in num if x not in special] == []:
        return "Special!!"
    else:
        return "NOT!!"