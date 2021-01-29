from itertools import permutations,combinations

a = [0,1,2,3,4,5,6,7]
comb = list(combinations(a,4))
for k in range(len(comb)//2):
    print(comb[k])
    print(comb[len(comb)-k-1])

