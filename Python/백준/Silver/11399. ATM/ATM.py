import sys
input = sys.stdin.readline

def sum_ppl(idx):
    tot = 0
    for i in range(idx):
        tot += ppl[i]

    return tot + ppl[idx]

N = int(input())
ppl = list(map(int, input().split()))
ppl.sort()
all_tot = 0

for i in range(N):
    all_tot += sum_ppl(i)

print(all_tot)
