from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    w = 0 # 다리 무게
    
    bridge = deque()
    
    while truck_weights or bridge:
        time += 1
        if bridge:
            cur_w, cur_t = bridge[0]
            if (time - cur_t) >= bridge_length:
                bridge.popleft()
                w -= cur_w
                
        if truck_weights:
            n = truck_weights[0]
            if w + n <= weight and len(bridge) + 1 <= bridge_length:
                bridge.append((n, time))
                w += n
                truck_weights.pop(0)  
    return time