numbers = [4,5,6,1,9]
n = len(numbers)
k = 3

ret = []
def combination(idx):

    if len(ret) == k:
        print(ret)
    for i in range(idx,n):
        ret.append(numbers[i])
        combination(i+1)
        ret.pop()
combination(0)