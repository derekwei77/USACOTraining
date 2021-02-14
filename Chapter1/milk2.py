"""
ID: derekwe1
LANG: PYTHON3
TASK: milk2
"""
import math

intervals = []

with open('milk2.in', 'r') as fin:
    lines = fin.readlines()

    for i in range(1, len(lines)):
        interval = map(int, lines[i].strip().split())
        intervals.append(interval)

maxTime -= 1
count = [0] * (maxTime)

longestMilkTime = 0
longestNonMilkTime = 0

print(minTime)
print(maxTime)

for i in range(len(startTimes)):
    start = startTimes[i] - 1
    end = endTimes[i] - 1
    for j in range(start, end):
        count[j] += 1

i = minTime - 1
while (i < maxTime):
    milkTime = 0
    while (i < maxTime and count[i] > 0):
        milkTime += 1
        i += 1
    if (longestMilkTime < milkTime):
        longestMilkTime = milkTime
    
    nonMilkTime = 0
    while (i < maxTime and count[i] == 0):
        nonMilkTime += 1
        i += 1
    if (longestNonMilkTime < nonMilkTime):
        longestNonMilkTime = nonMilkTime

print(longestMilkTime)
print(longestNonMilkTime)
with open('milk2.out', 'w') as fout:
    outputStr = str(longestMilkTime) + ' ' + str(longestNonMilkTime) + '\n'
    lines = fout.write(outputStr)
