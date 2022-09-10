def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    finish = []
    bridge = []
    
    while truck_weights:
        n = truck_weights[0]
        answer += 1
        if bridge:
            finish.append(bridge[0])
            bridge.pop(0)
        if sum(bridge) + n <= weight:
            bridge.append(n)
            truck_weights.pop(0)
            
            
    return answer