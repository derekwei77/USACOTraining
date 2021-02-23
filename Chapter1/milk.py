"""
ID: derekwe1
LANG: PYTHON2
PROG: milk
"""

def takeFirst(element):
    return element[0]

with open('milk.in', 'r') as fin:
    N, M = map(int, fin.readline().split())
    farmers = []
    for i in range(M):
        P_i, A_i = map(int, fin.readline().split())
        farmers.append((P_i, A_i))

farmers.sort(key=takeFirst)
print(farmers)

cost = 0
for farmer in farmers:
    price = farmer[0]
    amount = min(farmer[1], N)
    cost += price * amount
    N -= amount
    if N == 0:
        break

print(cost)
with open('milk.out', 'w') as fout:
    fout.write(str(cost) + '\n')