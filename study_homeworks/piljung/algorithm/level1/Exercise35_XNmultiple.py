# 35. X만큼 간격이 있는 N개의 숫자

def solution(x, n):
    answer = []

    for m in range(1, n + 1):
        answer.append(x * m)

    return answer