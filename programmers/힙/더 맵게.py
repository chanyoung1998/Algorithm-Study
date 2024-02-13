from heapq import heappop,heappush,heapify


def solution(scoville, K):
    answer = 0
    heapify(scoville)

    while scoville:

        if scoville[0] >= K:
            return answer

        if len(scoville) >= 2:

            heappop1 = heappop(scoville)
            heappop2 = heappop(scoville)
            heappush(scoville, heappop1 + 2 * heappop2)
            answer += 1
        else:
            return -1

scoville = [1, 2,3]
K = 7
print(solution(scoville,K))