import sys


def stringCompression(s):
    answer = sys.maxsize
    #comp 단위
    for step in range(1,len(s)//2 + 1):
        compressed = ''
        prev = s[:step]
        count = 1
        for j in range(step,len(s),step):
            if prev == s[j:j + step]:
                count += 1
            else:
                if count != 1:
                    compressed += str(count) + prev
                else:
                    compressed += prev
                prev = s[j:j+step]
                count = 1

        if count != 1:
            compressed += str(count) + prev
        else:
            compressed += prev
        answer = min(answer,len(compressed))
        print(compressed)
    return answer
print(stringCompression("abcabcababa"))