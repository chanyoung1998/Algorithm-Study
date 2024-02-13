def solution(arr):
    answer = []


    for i in arr:
        if not answer:
            answer.append(i)
        else:
            if answer[-1] == i:
                continue
            else:
                answer.append(i)

    return answer


