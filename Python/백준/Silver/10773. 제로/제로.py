import sys
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    num = int(input())
    if num == 0 and stack:
        stack.pop()
    else:
        stack.append(num)
        
print(sum(stack))