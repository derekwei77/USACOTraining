"""
ID: derekwe1
LANG: PYTHON3
TASK: namenum
"""
from collections import deque

numToLetters = {'2': 'ABC', '3': 'DEF', '4': 'GHI',
                '5': 'JKL', '6': 'MNO', '7': 'PRS',
                '8': 'TUV', '9': 'WXY'}

with open('namenum.in', 'r') as fin:
    originalNumber = fin.readline().strip()

with open('dict.txt', 'r') as fin:
    namesInDict = set(filter(lambda x: len(x) == len(originalNumber), fin.read().splitlines()))

letters = numToLetters[originalNumber[0]]
names = deque([])
for letter in letters:
    names.append(letter)
for i in range(1, len(originalNumber)):
    letters = numToLetters[originalNumber[i]]
    newNames = deque([])
    while (len(names) > 0):
        name = names.popleft()
        for letter in letters:
            newNames.append(name + letter)
    names = newNames

validNames = []
for name in names:
    if name in namesInDict:
        validNames.append(name)

print(validNames)
with open('namenum.out', 'w') as fout:
    if len(validNames) == 0:
        fout.write('NONE\n')
    else:
        for name in validNames:
            fout.write(name + '\n')