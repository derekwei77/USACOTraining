"""
ID: derekwe1
LANG: PYTHON3
TASK: palsquare
"""
import math

def isPalindrome(numberStr):
    reversedNumber = []
    for i in range(len(numberStr)):
        reversedNumber.append(numberStr[len(numberStr) - 1 - i])
    for i in range(len(numberStr)):
        if (numberStr[i] != reversedNumber[i]):
            return False
    return True

# convert a number from Base 10 to Base base
def tenToBase(number, base):
    numberInBase = []
    while number > 0:
        remainder = number % base
        if remainder >= 10:
            remainder = chr(remainder - 10 + ord('A'))
        number = math.floor(number / base)
        numberInBase.append(remainder)
    numberInBase.reverse()
    return numberInBase

def convertListToString(list):
    return ''.join(str(e) for e in list)

with open('palsquare.in', 'r') as fin:
    base = int(fin.readline().strip())

with open('palsquare.out', 'w') as fout:
    for i in range(1, 301):
        square = i * i
        squareInBase = tenToBase(square, base)
        if (isPalindrome(squareInBase)):
            numberInBase = convertListToString(tenToBase(i, base))
            out = numberInBase + ' ' + convertListToString(squareInBase) + '\n'
            print(out)
            fout.write(out)


