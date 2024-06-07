import sys 
input = sys.stdin.readline

arr = [0] * 1000001
N = int(input())

for i in range(2, N+1):
    arr[i] = arr[i-1] + 1
    
    if i%2 == 0:
        arr[i] = min(arr[i], arr[i//2]+1)
    if i%3 == 0:
        arr[i] = min(arr[i], arr[i//3]+1)
        
print(arr[N])