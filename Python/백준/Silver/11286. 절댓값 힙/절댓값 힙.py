'''
최소힙 사용, abs()를 사용하여 (절댓값, 숫자) 형식으로 힙에 값을 넣어줌
'''

from heapq import *
import sys
input = sys.stdin.readline

heap = []
for i in range(int(input())):
    num = int(input())
    if num:
        heappush(heap, (abs(num), num))
    else:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)