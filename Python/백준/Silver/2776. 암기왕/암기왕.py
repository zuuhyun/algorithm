import sys
input = sys.stdin.readline

def binary_search(arr, num):
    left, right = 0, N - 1
    while left <= right:
        mid = (left + right) //2
        if arr[mid] == num:
            return True
        elif arr[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return False

T = int(input())
for _ in range(T):
    N = int(input())
    note1 = sorted(map(int, input().split()))
    M = int(input())
    note2 = list(map(int, input().split()))

    for num in note2:
        if binary_search(note1, num):
            print(1)
        else:
            print(0)
