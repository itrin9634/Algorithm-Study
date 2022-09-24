def solution(line):
    pos = []
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            if a*d - b*c == 0:
                continue
            x = (b * f - e * d) / (a * d - b * c)
            y = (e * c - a * f) / (a * d - b * c)
            if x.is_integer() and y.is_integer():
                x, y = int(x), int(y)
                if (x, y) not in pos:
                    pos.append((x, y))
    x_min, x_max, y_min, y_max = min(pos)[0], max(pos)[0], min(pos, key = lambda x:x[1])[1], max(pos,key = lambda x: x[1])[1]
    
    star = [['.'] * abs(x_max - x_min + 1) for _ in range(abs(y_max-y_min+1))]
    
    for a, b in pos:
        x, y = abs(y_max - b), abs(x_min - a)
        star[x][y] = '*'
    
    for i, v in enumerate(star):
        star[i] = ''.join(v)
    
    return star