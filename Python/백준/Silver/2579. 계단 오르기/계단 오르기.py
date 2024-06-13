import sys
input = sys.stdin.readline

n = int(input())
stairs, dp = [0] * n, [0] * n
for i in range(n):
    stairs[i] = int(input())

if n == 1:
    print(stairs[0])
elif n == 2:
    print(stairs[0] + stairs[1])
else:
    dp[0] = stairs[0]
    dp[1] = stairs[0] + stairs[1]
    dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])

    for i in range(3,n):
        dp[i] = max(stairs[i] + stairs[i-1] + dp[i-3], stairs[i]+dp[i-2])

    print(dp[n-1])