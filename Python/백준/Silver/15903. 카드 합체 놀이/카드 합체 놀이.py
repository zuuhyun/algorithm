'''
카드에서 두장을 골라 가장 작은 값을 만드는게 목표 
카드 두장의 값을 같을 수 있으나 동일한 카드를 두번 더하는건 x
예) arr = [1,1,2,3] arr[0] + arr[1]은 가능 arr[0]+arr[0] 불가능
'''
from heapq import *
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
heapify(arr)
answer = []

for _ in range(m):
    c1 = heappop(arr)
    c2 = heappop(arr)
    heappush(arr, c1+c2)
    heappush(arr, c1+c2)

print(sum(arr))