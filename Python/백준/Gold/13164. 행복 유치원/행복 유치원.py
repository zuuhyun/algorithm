import sys
input = sys.stdin.readline

n, k = map(int, input().split())
student = list(map(int, input().split()))

height = []
for i in range(1, n):
    height.append(student[i] - student[i-1])

height.sort()
print(sum(height[:n-k]))