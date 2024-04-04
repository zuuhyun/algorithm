import sys
input = sys.stdin.readline

n = int(input())
num1 = list(map(int, input().split()))
visited = {}
for num in num1:
    visited[num] = 1

m = int(input())
num2 = list(map(int, input().split()))

for num in num2:
    print(visited.get(num, 0))