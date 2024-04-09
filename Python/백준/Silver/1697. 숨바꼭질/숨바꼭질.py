from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    queue = deque()
    queue.append(v)
    while queue:
        v = queue.popleft()
        if v == m:
            return visited[v]
        for next_v in [v-1, v+1, 2*v]:
            if next_v < 0 or next_v > 100000:
                continue
            if visited[next_v] == 0:
                visited[next_v] = visited[v] + 1
                queue.append(next_v)


n, m = map(int, input().split())
visited = [0] * 100001
print(bfs(n))