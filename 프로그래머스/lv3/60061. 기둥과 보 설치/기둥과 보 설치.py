def check(answer):
    for x, y, a in answer:
        if a == 0: #기둥
            if y == 0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
                continue
            return False
        else: #보
            if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1]in answer):
                continue
            return False  
    return True

def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y, a, b = build
        if b == 0: #삭제
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])
                
        else: #설치할 때
            answer.append([x, y, a])
            if not check(answer):
                answer.remove([x, y, a])                
    answer.sort()
    return answer