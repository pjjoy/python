def solution(n, lost, reserve):
    save = []

    if len(reserve) < len(lost):
        for lostst in lost:
            for reservest in reserve:
                if lostst == reservest - 1 or lostst == reservest + 1:
                    save.append(reservest)
    else:
        for lostst in lost:
            for reservest in reserve:
                if reservest == lostst - 1 or reservest == lostst + 1:
                    save.append(lostst)

    a = len(list(set(save)))  # 중복 제거
    answer = n - len(lost) + a

    return answer