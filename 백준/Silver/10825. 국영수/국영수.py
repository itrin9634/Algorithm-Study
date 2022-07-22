n = int(input())
students = []
for i in range(n):
    s = input().split()
    name, korean, english, math = s
    students.append([name, int(korean), int(english), int(math)])

sorted_students = sorted(students, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for s in sorted_students:
    print(s[0])