'''
K개의 랜선을 N개의 같은 길이의 랜선으로 만들고싶음
(N개보다 더 많이 만드는 것도 N개에 포함)

목표: 랜선을 N개로 만들 때 최대 랜선의 길이를 구하기
입력 
랜선의 개수, 필요한 랜선의 개수
각 랜선의 길이(한줄씩)
'''
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lines = [int(input()) for _ in range(k)]
left = 1
right = max(lines)

result = 0
while right >= left:
    mid = (right + left) // 2
    tot = 0
    for line in lines:
        tot += line // mid

    if tot >= n:
        result = mid
        left = mid + 1
    else:
        right = mid -1

print(result)