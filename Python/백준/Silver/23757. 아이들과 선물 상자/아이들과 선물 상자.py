import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
gifts = list(map(int, input().split()))
children = list(map(int, input().split()))
flag = False

new_gifts = []
for g in gifts:
    heapq.heappush(new_gifts, -g)

for child in children:
    gift = -(heapq.heappop(new_gifts))
    if gift < child:
        flag = True
        break
    gift -= child
    if gift != 0:
        heapq.heappush(new_gifts, -gift)

if flag:
    print(0)
else:
    print(1)