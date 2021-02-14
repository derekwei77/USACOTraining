"""
ID: derekwe1
LANG: PYTHON2
TASK: beads
"""

with open('beads.in', 'r') as fin:
    totalNumberOfBeads = int(fin.readline().strip())
    beads = fin.readline().strip()

doubleBeads = beads + beads
print(doubleBeads)
print(len(doubleBeads))

maxBeads = 0
for index in range(1, len(doubleBeads)):
    pos = index
    # print(pos)
    currentBeads = ''
    forwardNumber = 0
    while (pos < len(doubleBeads)):
        # print ('inside: ' + str(pos) + ': ' + doubleBeads[pos] + ':' + currentBeads)
        if (doubleBeads[pos] == 'w') or (currentBeads == '') or (doubleBeads[pos] == currentBeads):
            if (currentBeads == '' and doubleBeads[pos] != 'w'):
                currentBeads = doubleBeads[pos]
            pos += 1
            forwardNumber += 1
        else:
            break
    
    pos = index - 1
    currentBeads = ''
    backwardNumber = 0
    while (pos >= 0):
        if (doubleBeads[pos] == 'w') or (currentBeads == '') or (doubleBeads[pos] == currentBeads):
            if (currentBeads == '' and doubleBeads[pos] != 'w'):
                currentBeads = doubleBeads[pos]
            pos -= 1
            backwardNumber += 1
        else:
            break

    currentTotalNumber = min(forwardNumber + backwardNumber, totalNumberOfBeads)
    if maxBeads < currentTotalNumber:
        maxBeads = currentTotalNumber

with open('beads.out', 'w') as fout:
    print(maxBeads)
    fout.write(str(maxBeads) + '\n')