import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    heap = []
    dist = [1e9] * (n+1)

    dist[start] = 0
    heapq.heappush(heap, (dist[start],start))

    while heap:
        cost, current = heapq.heappop(heap)
        if dist[current] < cost:
            continue

        for node_idx, node_cost in road[current]:
            new_cost = cost + node_cost
            if new_cost < dist[node_idx]:
                dist[node_idx] = new_cost
                heapq.heappush(heap,(new_cost,node_idx))

    return dist

n, m, x = map(int, input().split())
road = [[] for _ in range(m+1)]
for _ in range(1, m+1):
    a, b, _cost = map(int, input().split())
    road[a].append((b,_cost))

answer = 0
for i in range(1, n+1):
    go = dijkstra(i)
    back = dijkstra(x)
    answer = max(answer, go[x]+back[i])

print(answer)