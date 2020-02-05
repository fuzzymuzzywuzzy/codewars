#https://www.codewars.com/kata/5a63948acadebff56f000018/train/python

def max_product(lst, n_largest_elements):
    lst.sort(reverse=True)
    result = 1
    for n in lst[0:n_largest_elements]:
        result *= n
    return result