"""
ID: derekwe1
LANG: PYTHON2
PROG: ride
"""

def convertStringToNumber(name):
    sum = 1
    print(name)
    for letter in name:
        sum *= ord(letter) - ord('A') + 1
    print(sum)
    return sum

fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')

comet = fin.readline().strip('\n')
group = fin.readline().strip('\n')

numForComet = convertStringToNumber(comet) % 47
numForGroup = convertStringToNumber(group) % 47

if numForComet == numForGroup:
    fout.write('GO\n')
else:
    fout.write('STAY\n')

fout.close()




