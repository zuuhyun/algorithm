import sys
input = sys.stdin.readline

n = int(input())
car = [input() for _ in range(n)]
cnt = 0
for _ in range(n):
    out = input()
    if car[0] != out:
        cnt += 1
        car.remove(out)
    else:
        car.pop(0)

print(cnt)