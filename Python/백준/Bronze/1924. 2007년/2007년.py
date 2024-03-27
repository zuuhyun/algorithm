m, d = map(int, input().split())

mon = [31, 28, 31, 30, 31, 30, 31,31, 30, 31, 30, 31]
week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

days = 0
for i in range(m-1):
    days += mon[i]

answer = (days + d) % 7

print(week[answer])