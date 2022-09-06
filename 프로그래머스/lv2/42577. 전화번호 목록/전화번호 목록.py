def solution(phone_book):
    answer = True
    phone_book.sort()
    before = ''
    if phone_book:
        before = phone_book[0]
    for i in range(1, len(phone_book)):
        if len(before) <= len(phone_book[i]):
            if phone_book[i][:len(before)] == before:
                answer = False
                break
        before = phone_book[i]
        
    return answer