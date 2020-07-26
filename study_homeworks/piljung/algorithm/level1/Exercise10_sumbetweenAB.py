def solution(a, b):
    answer = 0

    for i in range(min(a, b), max(a, b) + 1):
        answer += i

    return answer


###다른 풀이

def solution(a, b):

    if a > b:
        a, b = b, a   ## 이렇게 뒤집어서 정의 할 수 있다니...
    return sum(range(a,b+1))

