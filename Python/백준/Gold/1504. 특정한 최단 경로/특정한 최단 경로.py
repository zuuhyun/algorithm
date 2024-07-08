import heapq
import sys
INF = sys.maxsize
input = sys.stdin.readline
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a].append((w,b))
    graph[b].append((w,a))

x,y = map(int, input().split())

heap = []
def dik(start,end):
    heapq.heappush(heap, (0,start))
    dp = [INF] * (N + 1)
    dp[start] = 0
    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dp[node]:
            continue
        for next_cost, next_node in graph[node]:
            sum_cost = cost + next_cost
            if dp[next_node] > sum_cost:
                dp[next_node] = sum_cost
                heapq.heappush(heap, (sum_cost, next_node))
    return dp[end]

path1 = dik(1,x) + dik(x,y) + dik(y,N)
path2 = dik(1,y) + dik(y,x) + dik(x,N)

if path1 >= INF and path2 >= INF:
    print(-1)
else:
    print(min(path1, path2))