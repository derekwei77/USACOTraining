"""
ID: derekwe1
LANG: PYTHON2
TASK: friday
"""
import math

def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return (year % 400 == 0)

def updateNumberOf13s(year, firstDayPos, numberOf13s):
    daysOfAMonth = [31, -1, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for month in range(1, 13):
        if month == 2:
            if isLeapYear(year):
                daysInCurrentMonth = 29
            else:
                daysInCurrentMonth = 28
        else:
            daysInCurrentMonth = daysOfAMonth[month - 1]
        PositionOf13 = (12 + firstDayPos) % 7
        numberOf13s[PositionOf13] += 1
        firstDayPos = (daysInCurrentMonth + firstDayPos) % 7
    return firstDayPos

#Saturday, Sunday, ... Friday
numberOf13s = [0] * 7

with open('friday.in', 'r') as fin:
    numberOfYears = int(fin.readline().strip())
    firstDayPos = 2
    for i in range(numberOfYears):
        firstDayPos = updateNumberOf13s(1900 + i, firstDayPos, numberOf13s)

print(numberOf13s)
outputStr = ''
for number in numberOf13s:
    outputStr += str(number) + ' '
outputStr = outputStr.strip() + '\n'
with open('friday.out', 'w') as fout:
    fout.write(outputStr)