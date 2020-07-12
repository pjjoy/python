#일부 테스트 통과 못한 로직
def solution(n, lost, reserve):
    save = []
    resetlost = set(lost) - set(reserve)
    resetreserve = set(reserve) - set(lost)  # 여분있는 사람이 도난 당했을 경우 빌려줄 수 없으므로 삭제

    if len(resetreserve) <= len(resetlost):
        for lostst in resetlost:
            for reservest in resetreserve:
                if lostst == reservest - 1 or lostst == reservest + 1:
                    save.append(reservest)
    else:
        for lostst in resetlost:
            for reservest in resetreserve:
                if reservest == lostst - 1 or reservest == lostst + 1:
                    save.append(lostst)

    a = len(list(set(save)))  #
    answer = n - len(lost) + a

    return answer


#최종 풀이

def solution(n, lost, reserve):
    resetlost = set(lost) - set(reserve)
    resetreserve = set(reserve) - set(lost)  # 여분있는 사람이 도난 당했을 경우 빌려줄 수 없으므로 삭제
    for i in resetreserve:
        if i - 1 in resetlost:
            resetlost.remove(i - 1)
        elif i + 1 in resetlost:
            resetlost.remove(i + 1)

    return n - len(resetlost)