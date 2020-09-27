#. 39 실패율


#첫번째 풀이 ) 런타임 오류 존재

def solution(N, stages):
    failurerate = {}
    under = len(stages)

    for n in range(1, N + 1):
        failurerate[n] = stages.count(n) / under
        under = under - stages.count(n)

    answer = sorted(failurerate, reverse=True, key=lambda x: failurerate[x])  # 딕셔너러 람다 정렬

    return answer


#통과한 다른 사람의 답변... 무슨 미묘한 차이일까?


def solution(N, stages):
    result = {}
    num = len(stages)

    for stage in range(1, N+1):
        if num != 0:
            count = stages.count(stage)
            result[stage] = count / num
            num -= count
        else:
            result[stage] = 0

    return sorted(result, key=lambda x : result[x], reverse=True)
