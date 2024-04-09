'''
입력: 테스트케이스, 파일 갯수, 파일들...
출력: 파일을 하나로 합칠때 최소비용을 계산하는 프로그램

문제 접근 방법
heap 사용 pop() 해서 더하고 다시 넣어주기
'''

from heapq import *
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    files = int(input())
    heap = list(map(int, input().split()))
    heapify(heap)
    answer = []

    while len(heap) > 1:
        value = heappop(heap) + heappop(heap)
        heappush(heap, value)
        answer.append(value)

    print(sum(answer))