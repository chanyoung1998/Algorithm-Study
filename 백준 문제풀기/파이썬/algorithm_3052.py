'''
내용:백준 알고리즘 단계별 풀기 1차원 배열 3052번 나머지
날짜:21년1월8일
사용 언어:파이썬

set은 단순히  다음과 같이 선언할 수 없다. 이렇게 되면 dictionary와 동일한
중괄호를 사용하기 때문이다. 따라서 set()이란 생성자를 이용한다.
변수_이름  = { } ->dict
변수_이름  = set() ->set

s = set([1,3,5,7])->set
s = {1,3,5,7} ->set

'''

data_list = []
mod_set = set()

for i in range(10):
    data_list.append(int(input()))

for i in data_list:
    mod = i % 42
    mod_set.add(mod)

print(len(mod_set))



'''
다른 풀이 법

num_list = []

for i in range(10):
    num = int(input())
    num_list.append(num % 42)
    
num_list = set(num_list)
print(len(num_list))

'''
