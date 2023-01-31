def solution(s):
    answer = 0 #분해한 문자열의 갯수
    same = 0 # 같은 갯수
    diff = 0 # 다른 갯수
    first = s[0] # 처음 문자
    
    for i in range(len(s)):
        if s[i] == first:
            same += 1
        else:
            diff += 1
        
        if same == diff:
            answer += 1
            
            #값 초기화
            same = 0
            diff = 0
            if i != len(s)-1:
                first = s[i+1]
    # 딱 떨어지지 않는 것이 있는 경우
    if same != 0 or diff != 0:
        answer += 1
        
    return answer