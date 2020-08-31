# 24. 정수 내림차순으로 배치하기

def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))  #문자열로 리스트 정리하여 붙이기