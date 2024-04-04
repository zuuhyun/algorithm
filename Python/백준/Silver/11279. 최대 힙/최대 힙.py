from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a = int(input())
    if a:
        heappush(arr, -a)
    else:
        if arr:
            print(-heappop(arr))
        else:
            print(0)