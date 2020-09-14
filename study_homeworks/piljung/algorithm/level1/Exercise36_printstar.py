# 36. 직사각형 별찍기

a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print('*', end='')  # default가 end="\n" 이기 때문에 개행되지 않도록 설정
    print()

'''
(참고) print 함수 기능 : end, sep
print("010","1234","5678", sep="-") #출력: 010-1234-5678

'''

#. 다른 풀이
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)