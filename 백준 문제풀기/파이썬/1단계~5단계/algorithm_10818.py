'''
내용:백준 알고리즘 단계별 풀기 1차원 배열 10818번 최대 최소 구하기
날짜:21년1월8일
사용 언어:파이썬

 min(iterable) 함수 예제1 : 리스트 이용 a = [1, 2, 3] print(min(a)) # 반환 : 1
 min(iterable) 함수 예제2 : 문자열 이용 b = 'BlockDMask' print(min(b)) # 반환 : 'B'
 min(iterable) 함수 예제3 : non iterable 인 경우 c = 1 # print(min(c)) # error : 'int' object is not iterable
 min(iterable) 함수 예제4 : 튜플 이용 d = (6, 5, 4, 2) print(min(d))  # 반환 : 2
 min(iterable) 함수 예제5 : 리스트 이용2 e = [3, 4, 5, 'a', 'b', 'c'] # print(min(e)) # error : str 타입과 int 타입은 비교할 수 없기 때문

iterable 데이터 형식은 반복이 가능한 데이터 즉,member를 하나씩 반환(접근)할 수 있는 데이터 타입을 말합니다.

출처: https://blockdmask.tistory.com/411
'''

n = int(input())
array_list = list(map(int,input().split()))

print(min(array_list),max(array_list))

