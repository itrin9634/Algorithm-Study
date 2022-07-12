import heapq
def solution(food_times, k):
    h = []
    length = len(food_times)
    if sum(food_times) <= k :
        return -1
    sum_value = 0
    now, previous = 0, 0
    for i in range(len(food_times)):
        heapq.heappush(h, (food_times[i] , i+1))
    
    while sum_value + (h[0][0] - previous) * length <= k:
        now =  heapq.heappop(h)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    arr = sorted(h, key = lambda x: x[1])
    answer = arr[(k - sum_value) % length][1]
        
        
    return answer