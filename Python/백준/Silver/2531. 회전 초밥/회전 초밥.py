import sys
input = sys.stdin.readline
n, d, k, c = map(int, input().split())
dishes = [int(input()) for _ in range(n)] * 2

answer = 0
for i in range(n):
    eat = set(dishes[i:i+k])
    if c in eat:
        answer = max(answer, len(eat))
    else:
        answer = max(answer, len(eat)+1)

print(answer)