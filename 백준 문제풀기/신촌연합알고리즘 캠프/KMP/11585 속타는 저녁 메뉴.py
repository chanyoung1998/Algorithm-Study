import sys
import math
n = int(sys.stdin.readline().rstrip())
p = sys.stdin.readline().rstrip().split()
s = sys.stdin.readline().rstrip().split()
s = s + s[:-1]
#print(s)
def computeLPS(pat,lps):

    leng = 0
    # 항상 lps[0] == 0 이므로 while문은 i=1부터 시작
    i = 1

    while i < len(pat):

        if pat[i] == pat[leng]:
            leng += 1
            lps[i] = leng
            i += 1
        else:
            if leng != 0:
                leng = lps[leng-1]
            else:
                lps[i] = 0
                i += 1



def KMPSearch(pat, txt):
    M = len(pat)
    N = len(txt)
    count = 0
    lps = [0]*M

    # Preprocess the pattern
    computeLPS(pat, lps)

    i = 0  # index for txt[]
    j = 0  # index for pat[]
    while i < N:
        # 문자열이 같은 경우 양쪽 인덱스를 모두 증가시킴
        if pat[j] == txt[i]:
            i += 1
            j += 1
        # Pattern을 찾지 못한 경우
        elif pat[j] != txt[i]:
            # j!=0인 경우는 짧은 lps에 대해 재검사
            if j != 0:
                j = lps[j-1]
            # j==0이면 일치하는 부분이 없으므로 인덱스 증가
            else:
                i += 1

        # Pattern을 찾은 경우
        if j == M:
            #print("Found pattern at index " + str(i-j))
            # 이전 인덱스의 lps값을 참조하여 계속 검색
            j = lps[j-1]
            count += 1




    return count

c = KMPSearch(p,s)
gcd = math.gcd(c,n)

print(c//gcd,'/',n//gcd,sep='')