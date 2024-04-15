import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    dist = [INF] * (n+1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap,(dist[start],start))

    while heap:
        cost, current = heapq.heappop(heap)
        for next_idx, next_cost in graph[current]:
            new_cost = cost + next_cost
            if new_cost > m:
                continue
            if new_cost < dist[next_idx]:
                dist[next_idx] = new_cost
                heapq.heappush(heap, (new_cost,next_idx))

    return dist

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for _ in range(r):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))
    graph[y].append((x, cost))

result = []
for i in range(1, n+1):
    res = dijkstra(i)
    tmp = 0
    for idx, value in enumerate(res):
        if value != INF:
            tmp += items[idx]

    result.append(tmp)

print(max(result))