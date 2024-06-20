import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)
works = []
for _ in range(N):
    works.append(list(map(int, input().split())))

for i in range(N):
    time, pay = works[i]
    end_day = i + time
    if end_day <= N:
        dp[end_day] = max(dp[end_day], dp[i] + pay)
    
    dp[i+1] = max(dp[i+1], dp[i])

print(max(dp))