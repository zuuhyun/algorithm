grade_list = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5,
         'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}

grade = 0
credit = 0
tot_subject = []

while True:
    try:
        subject = list(input().split())
    except:
        break
    if len(subject) == 0:
        break
    tot_subject.append(subject)

for subject in tot_subject:
    if subject[2] != 'P':
        credit += float(subject[1])
        grade += grade_list[subject[2]] * float(subject[1])

print("{:0.6f}".format(grade/credit))