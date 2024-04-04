import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
answer = [-1] * n
count = [0] * 1000001
for num in nums:
    count[num] += 1

stack = []
for i in range(n):
    while stack and count[nums[stack[-1]]] < count[nums[i]]:
        answer[stack.pop()] = nums[i]
    stack.append(i)

print(*answer)