'''
힙사용
최대 힙으로 값 넣기
heappop() 한 값과 dasom 비교
heappop()한 값이 더 크면 dasom +1 cnt +1 heappop() 한 값 -1 
heappop()한 값 다시 넣어주기
'''
from heapq import *
import sys
input = sys.stdin.readline

n = int(input())
max_heap = []

for i in range(n):
    vote = int(input())
    if i == 0:
        dasom = vote
        continue
    heappush(max_heap, -vote)

cnt = 0
while max_heap:
    vote = -heappop(max_heap)
    if dasom > vote:
        break

    cnt += 1
    dasom += 1
    vote -= 1
    heappush(max_heap, -vote)

print(cnt)
