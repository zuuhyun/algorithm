word_list = []
for i in range(int(input())):
    word_list.append(input())

answer_list = []
for i in range(int(input())):
    answer_list.append(input())

start, end, answer = '', '', ''

if len(word_list) == 1:
    print(*answer_list)
else:
    for i, word in enumerate(word_list):
        if word == '?':
            if i == 0:
                end = word_list[i+1][0]
            elif i == len(word_list) - 1:
                start = word_list[i-1][-1]
            else:
                start = word_list[i-1][-1]
                end = word_list[i+1][0]

    for word in answer_list:
        if word in word_list:
            continue
        if start and end:
            if start == word[0] and end == word[-1]:
                answer = word
        elif start and not end:
            if start == word[0]:
                answer = word
        elif not start and end:
            if end == word[-1]:
                answer = word

    print(answer)
