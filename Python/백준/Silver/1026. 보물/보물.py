import sys
input = sys.stdin.readline

N = int(input())
a = sorted(map(int, input().split()),reverse=True)
b = sorted(map(int, input().split()))

res = 0
for i in range(N):
    res += a[i]*b[i]

print(res)