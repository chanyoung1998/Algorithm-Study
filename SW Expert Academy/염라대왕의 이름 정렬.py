for t in range(int(input())):
    n = int(input())
    names = set()
    for _ in range(n):
        name = input()
        if name not in names:
            names.add(name)
    names = list(names)
    names.sort(key=lambda x:(len(x),x))
    print("#",t+1,sep='')
    for name in names:
        print(name)
