from collections import defaultdict

def solution(players, callings):
    al_dict = defaultdict(int)
    
    for i in range(len(players)):
        al_dict[players[i]] = i
        
    for i in range(len(callings)):
        call = callings[i]
        idx = al_dict[call]
        before = players[idx-1]
        players[idx], players[idx-1] = players[idx-1], players[idx]
        al_dict[call] -= 1
        al_dict[before] += 1
    return players