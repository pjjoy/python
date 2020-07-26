#15. 서울에서 김서방 찾기

'''
find 함수와 index함수의 차이

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

def solution(seoul):
    return "김서방은 {0}에 있다".format(seoul.index("Kim"))

