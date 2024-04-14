import heapq
import sys
input = sys.stdin.readline
def dijkstra(start,end):
    dist[_start] = 0
    heap = []
    heapq.heappush(heap, (dist[start], start))

    while heap:
        cost, node = heapq.heappop(heap)

        if node == end:
            break

        if dist[node] < cost:
            continue

        for next_node, next_cost in line[node]:
            new_cost = cost + next_cost
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(heap,(new_cost,next_node))

    return dist

city = int(input())
bus = int(input())
line = [[] for _ in range(city+1)]
dist = [1e9] * (city+1)

for i in range(bus):
    start, end, cost = map(int, input().split())
    line[start].append((end, cost))

_start, _end = map(int, input().split())
dijkstra(_start, _end)
print(dist[_end])