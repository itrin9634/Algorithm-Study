def solution(cards):
    answer = 0
    for i in range(len(cards)):
        visited = [False] * len(cards)
        k = i
        group1 = set()
        while not visited[k]:
            visited[k] = True
            group1.add(cards[k])
            k = cards[k] - 1
        tmp = set(cards) - group1
        for j in tmp:
            group2 = set()
            k = j - 1
            while not visited[k]:
                group2.add(cards[k])
                visited[k] = True
                k = cards[k] - 1
            answer = max(answer, len(group1) * len(group2))    
    return answer