import sys
input = sys.stdin.readline

N, M = map(int, input().split()) #나무 수, 가져가야하는 나무의 길이
trees = list(map(int,input().split()))
trees.sort()
left = 1
right = trees[-1]
answer = 0

while right >= left:
    mid = (right + left) // 2
    tot = 0
    for tree in trees:
        if tree > mid:
            tot += tree - mid

    if tot < M:
        right = mid - 1
    else:
        left = mid + 1
        answer = mid

print(answer)