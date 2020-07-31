'''
## 아스키 코드
종류          문자상수        아스키코드
숫자 문자       0~9             48~57
대문자          A~Z             65~90
소문자          a~z             97~122

ord() 문자 > 아스키 코드로 변환
chr() 아스키 코드 > 문자로 변환
'''


def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():   # 대소문자 확인(대문자)
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower(): # 대소문자 확인(소문자)
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s) #더하기