"""
ID: derekwe1
LANG: PYTHON3
TASK: dualpal
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

def checkDualPal(number):
    count = 0
    for base in range(2, 11):
        numberInBase = tenToBase(number, base)
        if (isPalindrome(numberInBase)):
            count += 1
        if (count >= 2):
            return True
    return False



with open('dualpal.in', 'r') as fin:    
    N, S = map(int, fin.readline().split())

count = 0
currentNumber = S + 1
dualPalList = []
while (True):
    if (checkDualPal(currentNumber)):
        count += 1
        dualPalList.append(currentNumber)
    if (count == N):
        break
    currentNumber += 1

print(dualPalList)
with open('dualpal.out', 'w') as fout:
    for number in dualPalList:
        fout.write(str(number) + '\n')