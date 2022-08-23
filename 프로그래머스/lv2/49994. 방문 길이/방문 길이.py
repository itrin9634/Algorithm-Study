def get_dir(s):
    d = 0
    if s == 'U':
        d = 0
    elif s == 'D':
        d = 1
    elif s == 'R':
        d = 2
    elif s == 'L':
        d = 3
    return d


def solution(dirs):
    answer = 0
    
    #U, D, R, L
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    x, y = 0,0
    
    visited = []
    for d in dirs:
        i = get_dir(d)
        nx = x + dx[i]
        ny = y + dy[i]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if [(x, y), (nx, ny)] in visited or [(nx, ny), (x, y)] in visited:
                pass
            else:
                visited.append([(x, y), (nx, ny)])
                answer += 1
            x, y = nx, ny
    return answer