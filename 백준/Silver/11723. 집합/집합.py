import sys
input = sys.stdin.readline


def add_x(x):
    global s
    s.add(x)


def remove_x(x):
    global s
    s.discard(x)


def check_x(x):
    if x in s:
        print(1)
    else:
        print(0)
    return


def toggle_x(x):
    global s
    if x in s:
        s.remove(x)
    else:
        s.add(x)


def all():
    global s
    s = {i for i in range(1, 21)}


def empty():
    global s
    s = set()


m = int(input())
s = set()

for i in range(m):
    arr = input().split()
    if len(arr) == 2:
        x = int(arr[1])
    if arr[0] == 'add':
        add_x(x)
    if arr[0] == 'remove':
        remove_x(x)
    if arr[0] == 'check':
        check_x(x)
    if arr[0] == 'toggle':
        toggle_x(x)
    if arr[0] == 'all':
        all()
    if arr[0] == 'empty':
        empty()
