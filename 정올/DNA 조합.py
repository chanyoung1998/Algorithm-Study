import sys

n = int(sys.stdin.readline())
dna = [sys.stdin.readline().rstrip() for _ in range(n)]
visit = [False for _ in range(n)]
ret = 9999

def check(dna):

    return len(dna) <= ret

def dfs(i,connected_dna):
    global ret


    if i == n:
        print(connected_dna)
        ret = min(ret,len(connected_dna))
        return

    for k in range(n):
        if visit[k]:
            continue

        s1 = connected_dna
        s2 = dna[k]

        max_len = 0
        for j in range(1,len(s2)+1):
            target = s2[:j]
            cmp = s1[-j:]

            if j > len(s1):
                break
            if target == cmp:

                max_len = j

        # print(s1,s2[max_len:])
        new_connect_dna = s1 + s2[max_len:]

        if check(new_connect_dna):
            visit[k] = True
            dfs(i+1,new_connect_dna)
            visit[k] = False

    return

for i in range(n):
    visit[i] = True
    dfs(1,dna[i])
    visit[i] = False

print(ret)