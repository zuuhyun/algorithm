n = int(input())
top = list(map(int, input().split()))
stack = []
answer = [0] * n
for i in range(n):
    while stack:
        if top[i] < stack[-1][0]:
            answer[i] = stack[-1][1] + 1
            break
        else:
            stack.pop()
    stack.append([top[i],i])
print(*answer)
