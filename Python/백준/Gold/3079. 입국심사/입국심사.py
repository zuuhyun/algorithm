'''
이진탐색 
left = 0, right = 가장 오래걸리는 시간 * 사람수 mid = left+right // 2
mid 값을 각 심사대에서 심사를 받을 수 있는 사람의 수를 구하면서 
심사받을 수 있는 사람이 많으면 right 값을 mid 값으로 그 외에는 left 값을 mid + 1을 해서 
최소값을 구한다(left값)
'''
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
time = [int(input()) for _ in range(n)]
left = 0
right = max(time) * m
while right > left:
    mid = (left + right) // 2
    people = 0
    for t in time:
        people += mid // t
    if people >= m:
        right = mid
    else:
        left = mid + 1

print(left)