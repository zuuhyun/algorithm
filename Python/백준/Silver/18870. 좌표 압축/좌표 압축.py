'''
1. 리스트 값 받기 
2. 받은 값으로 새로운 리스트 생성 set() -> sorted()
3. 새로운 리스트로 딕셔너리 값을 만들어 준다. {리스트[0]:인덱스 값}
3. 기존 리스트를 key 값으로 딕셔너리에서 value 찾아 출력

list.index(i)의 형태는 시간복잡도 O(N)을 가지고 있고 
그렇다면 매번 최대 1,000,000번의 수행이 이루어지게 돼서 시간초과 발생
'''

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
uniq_arr = sorted(set(arr))
uniq_dic = {}
for idx, value in enumerate(uniq_arr):
    uniq_dic[value] = idx

for num in arr:
    print(uniq_dic[num], end=' ')