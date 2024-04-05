from heapq import *
import sys
input = sys.stdin.readline
heap = []
for _ in range(int(input())):
    cmd = list(map(int, input().split()))
    if len(cmd) == 1 and cmd[0] == 0:
        if heap:
            print(-heappop(heap))
        else:
            print(-1)
    else:
        for i in range(1, cmd[0]+1):
            heappush(heap, -cmd[i])