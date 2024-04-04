'''
y좌표가 건물의 높이로 건물의 높이가 낮아질 때마다 건물 갯수를 count
'''
import sys
input = sys.stdin.readline

n = int(input())
tot = 0
stack = []
for _ in range(n):
    x, y = map(int, input().split())
    while stack and stack[-1] > y:
        stack.pop()
        tot += 1

    if stack and stack[-1] == y:
        continue
    stack.append(y)
while stack:
    if stack[-1] > 0:
        tot += 1
    stack.pop()

print(tot)