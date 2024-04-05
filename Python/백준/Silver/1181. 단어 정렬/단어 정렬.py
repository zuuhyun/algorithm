import sys
input = sys.stdin.readline

n = int(input())
words = {input().strip() for _ in range(n)} #중복방지 set으로 생성
words = list(words) #정렬을 위해 list로 변환
words.sort(key=lambda x: (len(x),x)) #길이 순으로 정렬, 길이가 같다면 사전 순으로 정렬
for word in words:
    print(word)