def solution(numbers, target):
    answer = dfs(0,0,len(numbers),target,numbers)
    return answer


def dfs(x,cnt,N,target,numbers):

    if cnt == N:
        if x == target:
            return 1
        return 0
    else:
        return dfs(x + numbers[cnt],cnt+1,N,target,numbers) +  dfs(x - numbers[cnt],cnt+1,N,target,numbers)



print(solution([1,1,1,1,1],3))

