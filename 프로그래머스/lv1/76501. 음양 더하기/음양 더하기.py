def solution(absolutes, signs):
    answer = 0
    for val, sign in zip(absolutes, signs):
        if sign:
            answer += val
        else:
            answer -= val
    return answer