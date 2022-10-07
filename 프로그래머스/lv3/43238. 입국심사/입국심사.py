def solution(n, times):
    answer = max(times) * n
    left, right = 0, max(times) * n
    while right >= left:
        mid = (left + right) //2
        cnt = 0
        for t in times:
            cnt += (mid // t)
        if cnt < n:
            left = mid + 1
            continue
        answer = min(answer, mid)
        right = mid - 1    
    return answer