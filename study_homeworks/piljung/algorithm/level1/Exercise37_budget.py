# 37. 예산

def solution(d, budget):
    answer = 0

    d = sorted(d)  # 신청 금액이 작은 부서 부터 정렬
    sum = 0

    for i in d:
        if sum + i <= budget:
            sum += i
            answer += 1

    return answer