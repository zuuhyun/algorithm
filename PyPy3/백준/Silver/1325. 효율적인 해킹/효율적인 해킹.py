import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    queue = deque()
    queue.append(v)
    visited = [0] * (N + 1)
    visited[v] = 1
    cnt = 0

    while queue:
        v = queue.popleft()
        for x in graph[v]:
            if not visited[x]:
                cnt += 1
                visited[x] = 1
                queue.append(x)
    return cnt


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

max_cnt = 1
ret = []

for i in range(1, len(graph)):
    ret.append(bfs(i))

for i in range(len(ret)):
    if max(ret) == ret[i]:
        print(i+1, end=' ')