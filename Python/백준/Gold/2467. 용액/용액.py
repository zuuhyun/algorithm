import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

left = 0
right = n - 1
mix_sum = float('inf') #무한대로 초기화
result = (arr[left], arr[right])
while right > left:
    mid = arr[left] + arr[right]
    if abs(mid) < abs(mix_sum):
        mix_sum = mid
        result = (arr[left], arr[right])
        if mix_sum == 0:
            break
    if mid < 0:
        left += 1
    else:
        right -= 1

print(*result)