import sys

case = 1
while True:
    L,P,V = map(int,sys.stdin.readline().rstrip().split())
    if(L == 0 and P == 0 and V == 0):
        break

    print(f'Case {case}: {V // P * L + ((V % P) if L > (V%P) else L)}')
    case += 1