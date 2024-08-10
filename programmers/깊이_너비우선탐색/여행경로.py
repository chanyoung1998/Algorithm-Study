import sys
from collections import defaultdict,deque

sys.setrecursionlimit(5 ** 5)

ANSWER = 0
adjlist = defaultdict(list)

def solution(tickets):
    global ANSWER
    ANSWER = len(tickets) + 1

    for ticket in tickets:
        start = ticket[0]
        end = ticket[1]
        adjlist[start].append([end,False])

    for city in adjlist.keys():
        adjlist[city].sort()

    answer = []
    dfs('ICN', answer)
    return answer

def dfs(city, answer):
    global ANSWER
    answer.append(city)
    if len(answer) == ANSWER:
        return True

    for i in range(len(adjlist[city])):
        nextCity = adjlist[city][i][0]
        used = adjlist[city][i][1]
        if not used:
            adjlist[city][i][1] = True
            if dfs(nextCity,answer):
                return True
            adjlist[city][i][1] = False

    answer.pop()

    return False


# assert solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]) == ["ICN", "JFK", "HND", "IAD"]
# assert solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]) == ['ICN', 'ATL', 'ICN', 'SFO', 'ATL', 'SFO']
assert solution([["ICN", "AAA"], ["ICN", "CCC"], ["CCC", "DDD"], ["AAA", "BBB"], ["AAA", "BBB"], ["DDD", "ICN"], ["BBB", "AAA"]]) == ["ICN", "CCC", "DDD", "ICN", "AAA", "BBB", "AAA", "BBB"]
