#https://www.codewars.com/kata/5a4e3782880385ba68000018/train/python

def balanced_num(number):

    import math

    d = [int(x) for x in str(number)]

    if len(d) == 1:
        return "Balanced"

    elif len(d)%2 == 0:
        ref = int(len(d)/2)
        if sum(d[0:ref-1]) == sum(d[ref+1:len(d)]):
            return "Balanced"
        else:
            return "Not Balanced"

    else:
        ref = math.ceil((len(d)/2))
        if sum(d[0:ref-1]) == sum(d[ref:len(d)]):
            return "Balanced"
        else:
            return "Not Balanced"
