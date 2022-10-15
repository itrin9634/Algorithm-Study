from collections import defaultdict

def solution(n, results):
    answer = 0
    win_graph = defaultdict(set)
    lose_graph = defaultdict(set)
    
    for i in range(len(results)):
        a, b = results[i]
        win_graph[a].add(b) # 내가 이긴 애들
        lose_graph[b].add(a) # 내가 진 상대
    
    for i in range(1, n+1):
        for loser in win_graph[i]:
            lose_graph[loser] |= lose_graph[i]
        for winner in lose_graph[i]:
            win_graph[winner] |= win_graph[i]
            
        
    for i in range(1, n+1):
        if len(win_graph[i]) + len(lose_graph[i]) == n-1:
            answer += 1
    return answer