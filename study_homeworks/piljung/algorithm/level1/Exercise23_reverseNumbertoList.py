# 23. 자연수 뒤집어 배열로 만들기

def solution(n):
    new_n = [int(i) for i in str(n)]

    return list(reversed(new_n))