


def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    for i in range(len(prices)):

        if stack :

            curPrice = prices[i]

            while stack and curPrice < prices[stack[-1]]:
                popIndex = stack.pop()
                answer[popIndex] = i - popIndex

            stack.append(i)
        else:
            stack.append(i)

    while stack:
        popIndex = stack.pop()
        answer[popIndex] = len(prices) - popIndex -1


    return answer

assert solution([1, 2, 3, 2, 3]	) == [4,3,1,1,0]


