'''
내용:백준 알고리즘 단계별 풀기 분할 정복 1780 종이의 개수
날짜:21년2월23일
사용 언어:파이썬
'''
import sys


def paper_cut(paper):
    global count_0
    global count_1
    global count_minus1

    len_paper = len(paper)
    sum_paper = 0

    flag_0 = True
    flag_1 = True
    flag_minus = True

    for _ in range(len_paper):
        sum_paper += sum(paper[_])
        for i in paper[_]:
            if not flag_1 and not flag_0 and not flag_minus:
                break
            if i == 0 or i == 1:
                flag_minus = False
            if i == 0 or i == -1:
                flag_1 = False
            if i == 1 or i == -1:
                flag_0 = False

    if sum_paper == len_paper ** 2 and flag_1:
        count_1 += 1
        return
    elif sum_paper == -(len_paper**2) and flag_minus:
        count_minus1 += 1
        return
    elif sum_paper == 0 and flag_0:
        count_0 += 1
        return

    paper_cut([paper[i][:len_paper//3] for i in range(len_paper//3)])
    paper_cut([paper[i][len_paper // 3:len_paper//3 * 2] for i in range(len_paper // 3)])
    paper_cut([paper[i][len_paper // 3 * 2:] for i in range(len_paper // 3)])

    paper_cut([paper[i][:len_paper // 3] for i in range(len_paper//3,len_paper // 3 * 2)])
    paper_cut([paper[i][len_paper // 3:len_paper // 3 * 2] for i in range(len_paper//3,len_paper // 3 * 2)])
    paper_cut([paper[i][len_paper // 3 * 2:] for i in range(len_paper//3,len_paper // 3 * 2)])

    paper_cut([paper[i][:len_paper // 3] for i in range(len_paper // 3 * 2, len_paper)])
    paper_cut([paper[i][len_paper // 3:len_paper // 3 * 2] for i in range(len_paper // 3 * 2, len_paper)])
    paper_cut([paper[i][len_paper // 3 * 2:] for i in range(len_paper // 3 * 2, len_paper)])


n = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

count_0 = 0
count_1 = 0
count_minus1 = 0



paper_cut(paper)
print(count_minus1)
print(count_0)
print(count_1)



