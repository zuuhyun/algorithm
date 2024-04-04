from heapq import *
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    max_heap, min_heap = [], []
    n = int(input())
    visited = [1] * n
    for i in range(n):
        cmd, num = input().split()
        if cmd == 'I':
            heappush(min_heap, (int(num), i))
            heappush(max_heap, ((-(int(num)), i)))
        else:
            if num == '-1' and min_heap:
                visited[heappop(min_heap)[1]] = 0
            elif num == '1' and max_heap:
                visited[heappop(max_heap)[1]] = 0

        while min_heap and visited[min_heap[0][1]] == 0:
            heappop(min_heap)
        while max_heap and visited[max_heap[0][1]] == 0:
            heappop(max_heap)

    if min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')