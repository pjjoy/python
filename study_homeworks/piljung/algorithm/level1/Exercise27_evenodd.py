# 27. 짝수와 홀수

def solution(num):
    if num == 0 or num % 2 == 0:
        answer = "Even"
    else:
        answer = "Odd"

    return answer