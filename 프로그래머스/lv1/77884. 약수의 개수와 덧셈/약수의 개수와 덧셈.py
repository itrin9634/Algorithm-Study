def solution(left, right):
    arr = [i for i in range(left, right+1)]
    answer = sum(arr)

    for i in arr:
        if (i ** 0.5).is_integer():
            answer -= (i*2)
        
    return answer