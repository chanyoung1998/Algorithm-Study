import sys

sys.setrecursionlimit(5**5)

WORDS = ['A','E','I','O','U']
ANSWER = [-1,-1,-1,-1,-1]
curWord = [-1,-1,-1,-1,-1]
cnt = 0
answer = 0
def solution(word):
    global cnt

    for i in range(len(word)):
        for j in range(5):
            if word[i] == WORDS[j]:
                ANSWER[i] = j
                break
    print(ANSWER)
    dfs(0)
    return  answer

def dfs(idx):
    global cnt
    global answer
    if checkAnswer():
        answer = cnt

    print(curWord)
    if idx == 5:
        return

    for i in range(5):
        curWord[idx] = i
        cnt += 1
        dfs(idx+1)
    curWord[idx] = -1






def checkAnswer():

    for i in range(5):
        if ANSWER[i] != curWord[i]:
            return False

    return True


assert solution("AAAAE") == 6
# assert solution("AAAE") == 10
# assert solution("I") == 1563
# assert solution("EIO") == 1189

