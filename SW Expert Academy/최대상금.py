def dfs(count):
    global ret
    if not count:
        temp = int(''.join(numbers))
        ret = max(ret,temp)
        return

    for i in range(length):
        for j in range(i+1,length):
            numbers[i],numbers[j] = numbers[j],numbers[i]
            temp = int(''.join(numbers))
            if (temp,count-1) not in visit:
                visit.add((temp,count-1))
                dfs(count-1)
            numbers[i],numbers[j] = numbers[j],numbers[i]









for t in range(int(input())):
    numbers, change = map(int,input().rstrip().split())
    length = len(str(numbers))
    numbers = list(str(numbers))
    visit = set()
    ret = 0
    dfs(change)
    print('#{} {}'.format(t+1,ret))