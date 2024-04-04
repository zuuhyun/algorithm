import sys
input = sys.stdin.readline

n = int(input())
num = [int(input()) for _ in range(n)]
num.sort()

num_sum = set()
for x in num:
    for y in num:
        num_sum.add(x+y)

for i in range(n-1, -1, -1):
    for j in range(i+1):
        if num[i] - num[j] in num_sum:
            print(num[i])
            exit(0)