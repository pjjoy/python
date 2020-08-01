'''
#############################################################################################################
14. <<문자열 다루기 기본>>

[문제 설명]
String형 배열 seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하는 함수, solution을 완성하세요. seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

[제한 사항]
seoul은 길이 1 이상, 1000 이하인 배열입니다.
seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
Kim은 반드시 seoul 안에 포함되어 있습니다.

[입출력 예]
seoul	        return
[Jane, Kim]	    김서방은 1에 있다

#############################################################################################################
'''

def solution(seoul):
    return "김서방은 {0}에 있다".format(seoul.index("Kim"))


'''
###find 함수와 index함수의 차이

1. 찾는 문자열이 없을때 리턴하는 값이 다름
find : -1
index : error

2. find는 format으로 안감싸짐???( 상세 이유 확인 필요)
a="abcd"
an1=a.find('b')
an2=a.index('b')

print(an1)
print(an2)
print(type(an1))
print(type(an2))

<결과>
1
1
<class 'int'>
<class 'int'>

'''