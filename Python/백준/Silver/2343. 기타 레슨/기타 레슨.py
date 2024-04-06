import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lessons = list(map(int, input().split()))

left = max(lessons)
right = sum(lessons)
answer = right

while right >= left:
    mid = (right + left) // 2
    cnt = 1 #블루레이
    total = 0 #블루레이에 저장되는 시간

    for lesson in lessons:
        if total + lesson <= mid:
            total += lesson
        else:
            cnt += 1
            total = lesson

    if cnt <= M:
        answer = min(answer, mid)
        right = mid -1
    else:
        left = mid + 1

print(answer)