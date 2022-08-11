import math


def get_fee(minutes, fees):
    return fees[1] + math.ceil(max(0, float((minutes - fees[0]))) / fees[2] ) * fees[3]

def solution(fees, records):
    answer = []
    parking = dict()
    stack = dict()
    print(get_fee(334, fees))
    for record in records:
        time, car, cmd = record.split()
        h, m = time.split(":")
        minute = int(h) * 60 + int(m)
        if cmd == 'IN':
            parking[car] = minute
        elif cmd == 'OUT':
            try:
                stack[car] += minute - parking[car]
            except:
                stack[car] = minute - parking[car]
            del parking[car]
    
    last = 23 * 60 + 59
    for car, time in parking.items():
        try:
            stack[car] += last - parking[car]
        except:
            stack[car] = last - parking[car]
    print(stack)
    
    arr = []
    for car, times in stack.items():
        arr.append((car, times))
    arr.sort()
    for car, times in arr:
        answer.append(get_fee(times, fees))
        
    return answer