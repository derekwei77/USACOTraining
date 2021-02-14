"""
ID: derekwe1
LANG: PYTHON2
TASK: gift1
"""
import math

moneyAccount = {}
persons = []
with open('gift1.in', 'r') as fin:
    lines = fin.readlines()
    NP = int(lines[0].strip()) # NP number of persons
    for i in range(1, NP + 1):
        print(lines[i].strip())
        person = lines[i].strip()
        moneyAccount[person] = 0
        persons.append(person)
    pos = NP + 1
    while (pos + 1 < len(lines)):
        giver = lines[pos].strip()        
        total, numOfPersons = map(int, lines[pos+1].strip().split())
        if (numOfPersons > 0):
            moneyPerPerson = math.floor(total / numOfPersons)
            remaining = total - moneyPerPerson * numOfPersons
            moneyAccount[giver] -= (total - remaining)
            for i in range(1, numOfPersons + 1):
                receiver = lines[pos + 1 + i].strip()
                moneyAccount[receiver] += moneyPerPerson
        pos += 2 + numOfPersons
        print('update')
        for person in persons:
            print(person + ' ' + str(moneyAccount[person]))
        print('\n')

with open('gift1.out', 'w') as fout:
    for person in persons:
        fout.write(person + ' ' + str(int(moneyAccount[person])) + '\n')

