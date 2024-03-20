'''
24 03 20
거짓말
1043
분리 집합, 재귀. 그래프
진실을 아는 사람들이 속한 파티에 있는 사람들도 진실을 안다!
'''

import sys

n,m = map(int,sys.stdin.readline().strip().split(' '))
knowTruth = list(map(int,sys.stdin.readline().strip().split(' ')))[1:]
parties = []
for _ in range(m):
    party = set(list(map(int,sys.stdin.readline().strip().split(' ')))[1:])
    parties.append(party)


lieParty = [False for _ in range(m)] # 진실을 아는 파티
liePeople = [False for _ in range(n+1)] # 진실을 아는 사람들

def knowLie(x):

    if liePeople[x]:
        return

    liePeople[x] = True
    for i, party in enumerate(parties):
        if x in party:
            if not lieParty[i]:
                lieParty[i] = True
                for person in party:
                    knowLie(person)

    return

for kt in knowTruth:
    knowLie(kt)

print(m - sum(lieParty))