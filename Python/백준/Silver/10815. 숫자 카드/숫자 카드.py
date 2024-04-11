import sys
input = sys.stdin.readline
N = int(input())
card_list = list(map(int, input().split()))
card = {}
for c in card_list:
    card[c] = 1
M = int(input())
check = list(map(int, input().split()))

answer = []
for c in check:
    if card.get(c):
        answer.append(1)
    else:
        answer.append(0)
        
print(*answer)