import sys
input = sys.stdin.readline

n,m = map(int, input().split())
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

diff1 = set1 - set2
diff2 = set2 - set1
print(len(diff1)+len(diff2))