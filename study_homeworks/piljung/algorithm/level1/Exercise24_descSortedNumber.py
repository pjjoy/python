# 24. 정수 내림차순으로 배치하기

def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))  #문자열로 새로운 리스트 정렬하여 생성한 다음(* sorted : 신규리스트생성) join으로 정리하여 붙이기