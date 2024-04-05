'''
값을 받아 정렬 후 이진 탐색 
인덱스를 사용해서 배열의 값을 양 끝에서 부터 더해주고 
abs()를 사용하여 작은 값을 저장, 제일 작은 값의 리스트[left], 리스트[right]의 정보를 저장
'''
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

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