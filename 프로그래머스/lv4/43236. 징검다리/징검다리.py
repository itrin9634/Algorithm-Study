def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    dists = [rocks[0]]
    before = 0
    for i in range(1, len(rocks)):
        dists.append(abs(rocks[i] - rocks[i-1]))
    dists.append(abs(rocks[-1] - distance))
    print(dists)
    return answer