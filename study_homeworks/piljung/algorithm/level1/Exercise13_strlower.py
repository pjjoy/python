# 13.문자열 내림차순으로 배치하기

def solution(s):
    sortedlistS = sorted(list(s), reverse=True) #새로운 정렬 리스트를 정의할 때는 sorted / 그냥 기존 리스트 정렬시에는 sort

    answer = "".join(sortedlistS)

    return answer