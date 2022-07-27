def solution(new_id):
    answer = ''
    
    new_id = new_id.lower() # 소문자로 치환 1단계
    for i in range(len(new_id)):
        cur = new_id[i]
        if cur.isdigit() or cur.isalpha() or cur == '-' or cur == '_' or cur == '.': #2단계 & 3
            if answer and (answer[-1] == '.' and cur == '.'): # 3단계
                continue
            answer += cur
        else:
            continue
            
    #4단계
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    
    # 5단계
    if not answer:
        answer += 'a'
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7단계
    if len(answer) <= 2:
        answer = answer + ((answer[-1]) * (3 - len(answer)))
    
    return answer