n = int(input())
n_list = list(map(int, input().split()))
card = {}
for c in n_list:
    if card.get(c):
        card[c] += 1
    else:
        card[c] = 1

m = int(input())
m_list = list(map(int, input().split()))
for c in m_list:
    if card.get(c):
        print(card[c], end=" ")
    else:
        print('0', end=" ")