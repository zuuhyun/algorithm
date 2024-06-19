import sys
input = sys.stdin.readline

N,D = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dist = [i for i in range(D+1)]
for i in range(D+1):
    for start, end, cost in graph:
        dist[i] = min(dist[i], dist[i-1]+1)
        if start == i and end <= D and dist[start] + cost < dist[end]:
            dist[end] = dist[start] + cost

print(dist[D])