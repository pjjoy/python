# 25. 정수 제곱근 판별

import math


def solution(n):
    x = math.sqrt(n)

    if int(x) == x:
        answer = (x + 1) * (x + 1)
    else:
        answer = -1
    return answer