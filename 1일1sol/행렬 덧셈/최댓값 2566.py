import sys

max_row = 0
max_col = 0
max_val = 0
for i in range(9):
    inputs = list(map(int,input().split()))
    max_temp = max(inputs)

    if max_val < max_temp:
        max_val= max_temp
        max_row = i
        max_col = inputs.index(max_temp)

print(max_val)
print(max_row+1 , max_col+1)