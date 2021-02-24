"""
ID: derekwe1
LANG: PYTHON3
PROG: barn1
"""

stallsNum = []
with open('barn1.in', 'r') as fin:
    M, S, C = map(int, fin.readline().split())
    print([M, S, C])
    for i in range(C):
        stallsNum.append(int(fin.readline().strip()))
   
stallsNum.sort()
print(stallsNum)

if M >= C:
    total = C
else:
    total = stallsNum[len(stallsNum) - 1] - stallsNum[0] + 1
    gapsList = []
    for i in range(len(stallsNum) - 1):
        gap = stallsNum[i+1] - stallsNum[i]
        if gap > 1:
            gapsList.append(gap - 1)
    gapsList.sort(reverse = True)
    M = M - 1
    while(M > 0 and len(gapsList) > 0):
        gap = gapsList.pop(0)
        M -= 1
        total -= gap

print(total)
with open('barn1.out', 'w') as fout:
    fout.write(str(total) + '\n')