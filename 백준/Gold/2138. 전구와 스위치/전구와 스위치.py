from sys import stdin
import copy

n = int(input())
A = list(map(int, stdin.readline().rstrip()))
B = list(map(int, stdin.readline().rstrip()))

r1 = copy.deepcopy(A)
r2 = copy.deepcopy(A)

def two_flip(i, j):
    A[i] = 1 - A[i]
    A[j] = 1 - A[j]


def three_flip(i, j, k):
    A[i] = 1 - A[i]
    A[j] = 1 - A[j]
    A[k] = 1 - A[k]

for i in range(2):
    A = r1 if i == 0 else r2

    cnt = 0
    for j in range(n):
        if j == 0:
            if i == 0 and A != B:
                cnt += 1
                two_flip(j, j+1)
        elif 1 <= j <= n-2:
            if A[j-1] != B[j-1]:
                cnt += 1
                three_flip(j-1, j, j+1)
        elif j == n-1:
            if A[j-1] != B[j-1]:
                cnt += 1
                two_flip(j-1, j)
    if A == B:
        print(cnt)
        break
if A != B:
    print(-1)