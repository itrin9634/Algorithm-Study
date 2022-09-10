def solution(prices):
    answer = []
    for i in range(len(prices)):
        now = prices[i]
        time = 0
        for j in range(i+1, len(prices)):
            time += 1
            if prices[j] < now:
                answer.append(time)
                break
        else:
            answer.append(time)
            
    return answer