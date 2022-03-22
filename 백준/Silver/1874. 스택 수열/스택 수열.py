n = int(input())
s = []
op = []
count = 0
temp = True
for i in range(n):
    num = int(input())
    while count < num:
        count += 1
        s.append(count)
        op.append("+")
    if s[-1] == num:
        s.pop()
        op.append("-")
    else:
        temp = False
if not temp:
    print("NO")
else:
    print("\n".join(op))

