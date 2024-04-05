'''
메모리 제한이 있어서 배열에 있는 모든 값을 넣는 방식으로 진행하면 메모리 초과가 발생
힙의 길이를 n으로 유지하면서 힙에 존재하는 최소값과 넣을 값을 비교
'''
from heapq import *
import sys

input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    arr = list(map(int, input().split()))
    for num in arr:
        if len(heap) < n:
            heappush(heap, num)
        else:
            if heap[0] < num:
                heappop(heap)
                heappush(heap, num)

print(heappop(heap))