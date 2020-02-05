#https://www.codewars.com/kata/5a53a17bfd56cb9c14000003/train/python

def disarium_number(number):
    num = [int(n) for n in str(number)]
    output = []

    for i, n in enumerate(num):
        output.append(n**(i+1))

    if sum(output) == number:
        return "Disarium !!"

    else:
        return "Not !!"