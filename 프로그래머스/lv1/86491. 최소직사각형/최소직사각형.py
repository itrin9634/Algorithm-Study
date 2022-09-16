def solution(sizes):
    answer = 0

    arr1 = [min(v, i) for (i, v) in sizes]
    arr2 = [max(i, v) for (i, v) in sizes]
    answer = max(arr1) * max(arr2)
    return answer