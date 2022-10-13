def solution(distance, rocks, n):
    answer = 0
    start, end = 0, distance
    rocks.sort()
    
    while start  <= end:
        cnt = 0
        mid = (start + end) // 2
        pre = 0
        for i in rocks:
            if i - pre < mid:
                cnt += 1
            else:
                pre = i
                
        if cnt > n:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
        
        
    return answer