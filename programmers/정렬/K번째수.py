def solution(array, commands):
    answer = []

    for start,end,pos in commands:
         answer.append(sorted(array[start-1:end])[pos-1])
    return answer


