import sys


def solution1급3차5번(phrases, second):
    answer = ''
    start = second % (14 + len(phrases))
    display = '______________' + phrases + '______________'
    print(display[start:start + 14])
    return




def solution1급3차6번(n):
    answer = 0
    prime = []
    prime.append(2)
    #squere(i)까지만 조사해도 된다.
    for i in range(3, n + 1, 2):
        flag = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                flag = False
                break
        if flag:
            prime.append(i)

    prime_n = len(prime)
    for i in range(0, prime_n - 2):
        for j in range(i + 1, prime_n - 1):
            for k in range(j + 1, prime_n):
                if prime[i] + prime[j] + prime[k] == n:
                    answer += 1

    return answer



def 단어세기():

    ret = dict()
    while True:
        inputs = list(sys.stdin.readline().rstrip().split())
        if inputs == ['END']:
            break

        for word in inputs:
            if word not in ret.keys():
                ret[word] = 1
            else:
                ret[word] += 1

    for word in ret.keys():
        print(word,":",ret[word])


array = [3,4,1,2]
ret = [0 for _ in range(3)]
def comb(idx,k):
    if k == 3:
        print(ret)
        return
    for i in range(idx,4):
        ret[k] = array[i]
        comb(i+1,k+1)


comb(0,0)