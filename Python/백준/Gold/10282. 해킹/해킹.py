import heapq
import sys
input = sys.stdin.readline
INF = sys.maxsize
def dijkstra(start):
    dist = [INF] * (n+1)
    dist[start] = 0
    heap = []
    heapq.heappush(heap, (dist[start],start))

    while heap:
        cost, current = heapq.heappop(heap)
        if cost > dist[current]:
            continue
        for next_node, next_cost in conn[current]:
            new_cost = next_cost + cost
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heapq.heappush(heap,(new_cost, next_node))

    return dist

T = int(input())
for _ in range(T):
    n, d, c = map(int, input().split())
    conn = [[] for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        conn[b].append((a,s))

    result = dijkstra(c)
    cnt, max_ans = 0,0
    for res in result:
        if res != INF:
            cnt += 1
            max_ans = max(max_ans, res)

    print(f'{cnt} {max_ans}')