#https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

def spin_words(sentence):
    output = []
    for word in sentence.split():
        if len(word) >= 5:
            output.append(word[len(word)::-1])
        else:
            output.append(word)
    return ' '.join(output)
