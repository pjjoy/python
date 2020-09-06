# 22. 자릿수 더하기

def solution(n):
    new_n = [int(i) for i in str(n)]  # for문 한줄 정리 / 문자로 잘라서 숫자로 넣기

    return sum(new_n)