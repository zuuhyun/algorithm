import sys
input = sys.stdin.readline

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))

queue = [0] * w
time = 0

while queue:
    time += 1
    queue.pop(0)
    if trucks:
        if sum(queue) + trucks[0] <= l:
            queue.append(trucks.pop(0))
        else:
            queue.append(0)
print(time)