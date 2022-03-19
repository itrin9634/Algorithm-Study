import sys
n = int(sys.stdin.readline())
queue = []

for i in range(n):
    s = sys.stdin.readline().split()
    if s[0] == "push":  # push
        queue.append(s[1])
    elif s[0] == "pop":
        if len(queue) > 0:
            print(queue.pop(0))
        else:
            print(-1)
    elif s[0] == "size":
        print(len(queue))
    elif s[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == "front":
        if len(queue) > 0:
            print(queue[0])
        else:
            print(-1)
    elif s[0] == "back":
        if len(queue) > 0:
            print(queue[-1])
        else:
            print(-1)
