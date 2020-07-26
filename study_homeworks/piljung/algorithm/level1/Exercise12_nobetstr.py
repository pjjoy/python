def solution(s):
    bigs = s.upper()  # 대문자로 치환

    if bigs.count('P') == bigs.count('Y'):
        answer = True
    else:
        answer = False

    return answer