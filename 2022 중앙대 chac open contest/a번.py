import sys

n = int(sys.stdin.readline())
binary_bit = [0 for _ in range(32)]
reversed_bit = []
idx = 31
while n >= 1:
    if n % 2 == 0:
        binary_bit[idx] = 0
    else:
        binary_bit[idx]= 1
    idx -= 1
    n = n // 2


for bit in binary_bit:
    reversed_bit.append(0 if bit == 1 else 1)


add = 1
for i in range(31,-1,-1):
    if reversed_bit[i] + add == 2:
        reversed_bit[i] = 0
        #add는 계속 1
    else:
        reversed_bit[i] = reversed_bit[i] + add
        add = 0


ret = 0
for i in range(32):
    if binary_bit[i] != reversed_bit[i]:
       ret += 1

print(ret)