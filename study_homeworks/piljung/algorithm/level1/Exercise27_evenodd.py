# 27. 짝수와 홀수

def solution(num):
    if num == 0 or num % 2 == 0:
        answer = "Even"
    else:
        answer = "Odd"

    return answer


-- 한줄 정리
def solution(num):
    return "Even" if num == 0 or num % 2 == 0 else "Odd"
