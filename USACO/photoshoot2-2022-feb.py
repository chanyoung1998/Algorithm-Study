import sys

filename = "inputs/"
for t in range(2,15):

    filename_in = filename +str(t) + ".in"
    filenmae_out = filename + str(t) +".out"
    in_f = open(filename_in,"r")
    out = open(filenmae_out,"r")

    n = int(in_f.readline().rstrip())
    original = list(map(int,in_f.readline().rstrip().split()))
    target = list(map(int,in_f.readline().rstrip().split()))
    target_position = [0 for _ in range(n)]

    for i in range(n):
        target_position[target[i]-1] = i

    A = [target_position[v-1] for v in original]

    cnt = 0
    max_tmp = -1
    for x in A:
        if x > max_tmp:
            max_tmp = x
            continue

        cnt += 1
    print(cnt)
    print("ans:",out.readline())

    in_f.close()
    out.close()
