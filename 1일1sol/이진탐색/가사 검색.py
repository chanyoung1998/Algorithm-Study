import bisect
def solution(words,queries):
    n = len(words)
    q = len(queries)
    words_normal = [[] for _ in range(10001)]
    words_reversed = [[] for _ in range(10001)]

    for word in words:
        words_normal[len(word)].append(word)
        words_reversed[len(word)].append(word[::-1])
    for i in range(10001):
        words_normal[i].sort()
        words_reversed[i].sort()

    words = []
    ret = []
    for i in range(q):
        query = queries[i]
        if query[0] == "?":
            words = words_reversed[len(query)]
            query = query[::-1]
        elif query[-1] == "?":
            words = words_normal[len(query)]


        a = bisect.bisect_left(words,query.replace("?",'a'))
        b = bisect.bisect_right(words,query.replace("?",'z'))

        count = b-a
        ret.append(count)

    return ret
'''
def check(word,query):

    if len(word) != len(query):
        return False
    else:
        for i in range(len(query)):
            if query[i] == '?':
                continue
            if query[i] == word[i]:
                continue
            elif query[i] != word[i]:
                return False
        return True




def binary_search_first(words,query,start,end):

    lo = start
    hi = end

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if check(words[mid],query):
            hi = mid
        else:
            lo = mid

    return hi


def binary_search_last(words, query, start, end):
    lo = start
    hi = end

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if check(words[mid],query):
            lo = mid
        else:
            hi = mid

    return lo

'''

print(solution(["frodo","front","frost","frozen","frame","kakao"],["fro??","????o","fr???","fro???","pro?"]))