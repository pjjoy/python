# 21. 이상한 문자 만들기

def solution(s):
    new_s = s.split(' ') # 리스트에 단어별로 담기
    answer = ''
    for word in new_s:
        for i, spell in enumerate(word):
            answer += spell.upper() if i % 2 == 0 else spell.lower()
        answer += ' '
    return answer[:-1]