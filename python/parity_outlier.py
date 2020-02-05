#https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python

def find_outlier(integers):
odd, even = 0, 0

for num in integers3:
    if num%2 == 0:
        even += 1
    else:
        odd += 1

if even > odd:
    num = [num for num in integers3 if num%2==1]

else:
    num = [num for num in integers3 if num%2==0]

    return num