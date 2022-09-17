def solution(brown, yellow):   
    a = 1
    b = 0
    
    while True:
        if (brown + yellow) // a * a == brown + yellow:
            b = (brown+yellow) // a
            if 2 * (a+b) -4 <= brown:
                return[max(a, b), min(a, b)]
        a += 1