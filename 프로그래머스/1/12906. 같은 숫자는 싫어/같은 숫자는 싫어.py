def solution(arr):
    b = [arr[0]]
    for i in range(1, len(arr)):
        if b[-1] != arr[i]:
            b.append(arr[i])
    return b