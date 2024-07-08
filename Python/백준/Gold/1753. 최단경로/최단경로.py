import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V + 1)]
dp = [INF]*(V+1)
heap = []
def dijstr(start):
    dp[start] = 0
    heapq.heappush(heap,(0,start))

    while heap:
        w, v = heapq.heappop(heap)

        if dp[v] < w:
            continue

        for next_w, next_node in graph[v]:
            tot_w = w + next_w
            if tot_w < dp[next_node]:
                dp[next_node] = tot_w
                heapq.heappush(heap,(tot_w, next_node))

for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((w,e))

dijstr(start)
for i in range(1, V+1):
    print("INF" if dp[i] == INF else dp[i])