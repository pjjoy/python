#14. 문자열 다루기 기본

#런타임 애러나는 내 풀이
def solution(s):
    if (len(s) == 4 or len(S) == 6) and s.isdigit():  # isdigit() : 문자열이 숫자인지 확인 /* 참고: 문자열이 문자가 아닌지 판별하는 함수 isalpha
        return True
    else:
        return False


#다른 사람 풀이 (늘여 쓰지 않아도 되는 군)
def solution(s):
    return s.isdigit() and (len(s) == 4 or len(s) == 6)