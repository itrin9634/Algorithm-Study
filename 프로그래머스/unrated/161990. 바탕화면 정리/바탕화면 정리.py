def solution(wallpaper):
    lx, ly, rx, ry = int(1e9), int(1e9), 0, 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                lx, ly, rx, ry = min(lx, i), min(ly, j), max(rx, i+1), max(ry, j+1)
    return [lx, ly, rx, ry]