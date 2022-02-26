import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    word = sys.stdin.readline().split()
    order = word[0]

    if order == "push":
        v = word[1]
        stack.append(v)
    elif order == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif order == "size":
        print(len(stack))
    elif order == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif order =="top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
