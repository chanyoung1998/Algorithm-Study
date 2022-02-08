
for t in range(int(input())):
    n,m = map(int,input().rstrip().split())
    flag = False
    binary = list(bin(m)[2:])
    binary = list(map(int,[0 for _ in range(30-len(binary))] + binary))

    # print(binary[-1:-n-1])
    if sum(binary[:-n-1:-1]) == n:
        print('#',t+1," ON",sep='')
    else:
        print('#', t + 1, " OFF", sep='')