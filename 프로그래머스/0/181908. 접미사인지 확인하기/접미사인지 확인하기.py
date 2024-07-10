def solution(my_string, is_suffix):
    answer = 0
    if my_string[::-1][:len(is_suffix)] == is_suffix[::-1]:
        answer = 1
    return answer