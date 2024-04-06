'''
모든 요청이 배정될 수 있는 경우 요청한 금액을 그대로 배정
모든 요청이 배정될 수 없는 경우 정수 상한액을 계산
    상한액 이상은 상한액 배정, 이하는 요청한금액 배정

mid 값을 기준으로 요청된 예산의 총합과 국가예산을 비교하며 상한액 찾기
'''
import sys
input = sys.stdin.readline

n = int(input())
city = list(map(int, input().split()))
budget = int(input())

if sum(city) <= budget:
    print(max(city))
    exit(0)

left = 1
right = budget
answer = 0
while right >= left:
    mid = (right + left) // 2
    total = 0
    for c in city:
        total += min(c, mid)

    if total <= budget:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)