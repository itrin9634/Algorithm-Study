import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        n = heapq.heappop(scoville)
        if n >= K:
            return answer
        elif scoville:
            answer += 1
            sec = heapq.heappop(scoville)
            heapq.heappush(scoville, n + sec * 2)
        else:
            return -1