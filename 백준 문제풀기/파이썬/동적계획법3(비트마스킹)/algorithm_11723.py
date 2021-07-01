import sys

m = int(sys.stdin.readline())
s = 0
for _ in range(m):
    cmd = sys.stdin.readline().rstrip()

    if cmd == 'all':
        s = (1 << 21) - 1
    elif cmd =='empty':
        s = 0
    else:
        cmd, x = cmd.split()
        x = int(x)
        if cmd == 'add':
            if s & 1 << x == 1:
                continue
            else:
                s = s | 1 << x

        elif cmd == 'remove':
            if s & 1 << x == 0:
                continue
            else:
                s = s & ~(1 << x)

        elif cmd == 'check':
            if s & 1 << x:
                print(1)
            else:
                print(0)

        elif cmd == 'toggle':
            s = s ^ (1 << x)

