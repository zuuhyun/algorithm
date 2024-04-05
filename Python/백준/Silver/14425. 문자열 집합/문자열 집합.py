import sys
input = sys.stdin.readline

n,m = map(int, input().split())
words = {}
for _ in range(n):
    words[input()] = 1

cnt = 0
for _ in range(m):
    if words.get(input()):
        cnt += 1

print(cnt)