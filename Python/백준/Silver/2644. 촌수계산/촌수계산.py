import sys
input = sys.stdin.readline

def bfs(start, end):
    visited[start] = False
    queue = [start]

    while queue:
        current = queue.pop(0)
        if current == end:
            return answer[current]

        for node in edge[current]:
            if visited[node] == False:
                queue.append(node)
                visited[node] = True
                answer[node] = answer[current] + 1

    return -1

n = int(input())
x, y = map(int, input().split())
visited = [False] * (n+1)
edge = [[] for _ in range(n+1)]
answer = [0] * (n+1)

for i in range(int(input())):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)

print(bfs(x,y))