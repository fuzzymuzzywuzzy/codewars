#https://www.codewars.com/kata/5a54e796b3bfa8932c0000ed/train/python

def jumping_number(number):
    num = [int(n) for n in str(number)]
    output = []

    if len(num) == 1:
        return "Jumping!!"

    for i, n in enumerate(num):
        if i == len(num)-1:
            output.append(0)
        else:
            output.append(abs(num[i]-num[i+1]))

    if sum(output) == len(num)-1:
        return "Jumping!!"

    else:
        return "Not!!"