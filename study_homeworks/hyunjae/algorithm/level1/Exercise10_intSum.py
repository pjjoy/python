"""
두 정수 a, b가 주어졌을 때 a와 b 사이에 속한 모든 정수의 합을 리턴하는 함수, solution을 완성하세요.
예를 들어 a = 3, b = 5인 경우, 3 + 4 + 5 = 12이므로 12를 리턴합니다.

제한 조건
a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
a와 b는 -10,000,000 이상 10,000,000 이하인 정수입니다.
a와 b의 대소관계는 정해져있지 않습니다.
입출력 예
a	b	return
3	5	12
3	3	3
5	3	12
"""
a = -3
b = 6

#[내 풀이] 어렵게 푼...
def solution(a, b):
    big = max(abs(a),abs(b))
    small = min(abs(a),abs(b))
    answer = ((big * (big + 1) - small *(small + ((a * b < 0) * 1 + (a * b >= 0) * (-1)))) / 2) * (
                (a + b > 0) * 1 + (a + b < 0) * (-1))
    print(answer)
    return answer

#쉬운 풀이
def solution1(a,b):
    if a > b : a, b = b, a
    print(sum(range(a,b+1)))
    return sum(range(a,b+1))

solution1(a,b)