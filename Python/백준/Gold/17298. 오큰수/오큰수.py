import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
answer = [-1] * n
stack = []
for i in range(n):
    while stack:
        if stack[-1][0] < num[i]:
            answer[stack[-1][1]] = num[i]
            stack.pop()
        else:
            break

    stack.append([num[i], i])
print(*answer)