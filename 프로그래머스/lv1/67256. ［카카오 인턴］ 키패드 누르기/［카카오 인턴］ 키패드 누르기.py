def solution(numbers, hand):
    if hand == 'left':
        hand = 'L'
    else:
        hand = 'R'
    answer = ''
    keypad = {1:(0,0), 2:(0,1), 3:(0,2), 4:(1, 0), 5:(1, 1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2), '*':(3,0), 
             0:(3,1), '#':(3,2)}
    lhx, lhy = 3, 0
    rhx, rhy = 3, 2
    ld, rd = 0, 0
    for i in range(len(numbers)):
        if numbers[i] in (1, 4, 7):
            answer += 'L'
            lhx, lhy = keypad[numbers[i]]
        elif numbers[i] in (3, 6, 9):
            answer += 'R'
            rhx, rhy = keypad[numbers[i]]
        else:
            cur_x, cur_y = keypad[numbers[i]]
            ld = abs(lhx - cur_x) + abs(lhy - cur_y)
            rd = abs(rhx - cur_x) + abs(rhy - cur_y)
            cur_hand = 'R'
            if ld == rd:
                cur_hand = hand
            elif ld < rd:
                cur_hand = 'L'
            answer += cur_hand
            if cur_hand == 'R':
                rhx, rhy = cur_x, cur_y
            else:
                lhx, lhy = cur_x, cur_y
        
    return answer