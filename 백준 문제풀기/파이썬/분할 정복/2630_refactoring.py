import sys
sys.setrecursionlimit(10000)
n = int(input())
paper = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

#recursive
white = 0
blue = 0

def cut_paper(paper):
    global white, blue
    len_paper = len(paper)
    sum_paper = 0
    for _ in range(len_paper):
        sum_paper += sum(paper[_])

    if sum_paper==len_paper**2:
        blue += 1
        return

    if sum_paper==0:
        white += 1
        return

    cut_paper([paper[i][:len_paper//2] for i in range(len_paper//2)])
    cut_paper([paper[i][len_paper//2:] for i in range(len_paper//2)])
    cut_paper([paper[i][:len_paper//2] for i in range(len_paper//2,len_paper)])
    cut_paper([paper[i][len_paper//2:] for i in range(len_paper//2,len_paper)])

cut_paper(paper)
print(white)
print(blue)