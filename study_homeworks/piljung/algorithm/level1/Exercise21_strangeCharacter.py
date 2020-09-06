#21 . 이상한 문자 만들기

def solution(s):
    new_s = s.split(' ')
    answer = ''
    for word in new_s:
        for i, spell in enumerate(word):
            answer += spell.upper() if i % 2 == 0 else spell.lower() #한줄로 if문 작성하는 방법 : 의미는 동일
        answer += ' ' # 단어 종료 시 공백 추가
    return answer[:-1] # 마지막 공백 제거
