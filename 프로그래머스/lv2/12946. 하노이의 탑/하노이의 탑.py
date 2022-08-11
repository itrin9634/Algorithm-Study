def move(start, des, mid, n, arr):
    if n == 1:
        arr.append([start, des])
        return arr
    move(start, mid, des, n-1, arr)
    move(start, des, mid, 1, arr)
    move(mid, des, start, n-1, arr)

def solution(n):
    answer = []
    move(1, 3, 2, n, answer)
    return answer