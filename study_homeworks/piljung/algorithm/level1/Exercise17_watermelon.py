#17. 수박수박수박수박수박수?

def solution(n):
    answer = ''

    for i in range(0, n):
        if i % 2 == 0:
            answer += "수"  # 문자도 더할수 있음
        else:
            answer += "박"
    return answer