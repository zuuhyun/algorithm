import sys
input = sys.stdin.readline

def sort_student(arr, stu):
    cnt = 0
    for st in arr:
        if stu < st:
            cnt += 1
    return cnt

for _ in range(int(input())):
    student = list(map(int, input().split()))
    cnt = 0
    res = []
    for i in range(1,len(student)):
        res.append(student[i])
        cnt += sort_student(res, student[i])
    print(student[0], cnt)