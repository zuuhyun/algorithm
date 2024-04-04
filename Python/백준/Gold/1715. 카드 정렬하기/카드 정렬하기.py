from heapq import *
import sys
input = sys.stdin.readline

cards = []
for _ in range(int(input())):
    heappush(cards, int(input()))

tot = 0
while len(cards) > 1:
    n1 = heappop(cards)
    n2 = heappop(cards)
    value = n1 + n2

    tot += value
    heappush(cards, value)

print(tot)