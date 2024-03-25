# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    for calledName in callings:
        i = players.index(calledName)
        players[i-1], players[i] = players[i], players[i-1] # 파이썬은 다중할당이 있어서 tmp를 사용하지 않아서 좋다.
    return players

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))
