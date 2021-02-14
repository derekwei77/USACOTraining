"""
ID: derekwe1
LANG: PYTHON3
TASK: milk2
"""
import math

def takeFirst(element):
    return element[0]

intervals = []

with open('milk2.in', 'r') as fin:
    lines = fin.readlines()

    for i in range(1, len(lines)):
        s, e = map(int, lines[i].strip().split())
        intervals.append((s, e))

intervals.sort(key=takeFirst)
print(len(intervals))

# practice merge intervals
mergedIntervals = []
currentInterval = intervals[0]
for interval in intervals:
    s, e = interval
    if (s > currentInterval[1]):
        mergedIntervals.append(currentInterval)
        currentInterval = interval
    elif (e > currentInterval[1]):
        currentInterval = (currentInterval[0], e)

mergedIntervals.append(currentInterval)
print(len(mergedIntervals))
print(mergedIntervals)

longestMilkTime = 0
longestNonMilkTime = 0

# practice find max number in a list
for i in range(len(mergedIntervals)):
    interval = mergedIntervals[i]
    currentMilkTime = interval[1] - interval[0]
    if (currentMilkTime > longestMilkTime):
        longestMilkTime = currentMilkTime
    if (i < len(mergedIntervals) - 1):
        nextInterval = mergedIntervals[i+1]
        currentNonMilktime = nextInterval[0] - interval[1]
        if (currentNonMilktime > longestNonMilkTime):
            longestNonMilkTime = currentNonMilktime

print(longestMilkTime)
print(longestNonMilkTime)
with open('milk2.out', 'w') as fout:
    outputStr = str(longestMilkTime) + ' ' + str(longestNonMilkTime) + '\n'
    lines = fout.write(outputStr)
