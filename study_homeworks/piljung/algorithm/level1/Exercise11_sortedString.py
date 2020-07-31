#11. 문자열 내 마음대로 정렬하기

def solution(strings, n):
    answer = sorted(sorted(strings), key=lambda strings: strings[n])  # sorted()는정렬 시 키를 지정할 수 있음음
    return answer

