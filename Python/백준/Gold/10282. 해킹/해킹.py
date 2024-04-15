import heapq
import sys
input = sys.stdin.readline
inf = sys.maxsize

def dijkstra(start):
    dist = [inf] * (n+1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap,(dist[start],start))

    while heap:
        cost, current = heapq.heappop(heap)
        if cost > dist[current]:
            continue

        for node_idx, node_cost in graph[current]:
            new_cost = cost + node_cost
            if new_cost < dist[node_idx]:
                dist[node_idx] = new_cost
                heapq.heappush(heap, (new_cost, node_idx))

    return dist



T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a,s))

    dist = dijkstra(c)
    cnt, time = 0, 0
    for value in dist:
        if value != inf:
            cnt += 1
            time = max(time, value)
    print(f'{cnt} {time}')