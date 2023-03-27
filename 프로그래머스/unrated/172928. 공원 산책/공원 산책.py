def solution(park, routes):
    x, y = -1, -1
    dir_dic = {'N': (-1, 0), 'S':(1,0), 'W':(0, -1), 'E': (0, 1)}
    
    #시작 위치 설정
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                x, y = i, j
                break
    print(x, y)
    
    for r in routes:
        flag = False
        op, n = r.split()
        dx, dy = x, y
        mx, my = dir_dic[op]
        
        for k in range(1, int(n)+1):
            dx, dy = x + mx * k, y + my * k
            if not(0 <= dx < len(park)) or not(0 <= dy < len(park[0])):
                flag = True
                break
            if park[dx][dy] == 'X':
                flag = True
                break
        if not flag:
            x, y = dx, dy
    return [x, y]