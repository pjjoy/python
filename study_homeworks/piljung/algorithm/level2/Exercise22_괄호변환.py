# 균형잡힌 괄호 문자열 판단
def balanced(p):
    num = 0
    for idx, val in enumerate(p):
        if val == '(':
            num += 1
        if val == ')':
            num -= 1
        if num == 0:
            return idx  # 항상 홀수 값 반환(0에서 시작하기 때문에)


# 올바른 괄호 문자열 판단
def right(p):
    temp = []
    for x in p:
        if x == '(':
            temp.append(x)
        else:
            if len(temp) == 0:  # 앞에 열려있는 (가 없으면 )가 들어오면 올바르지 않음
                return False
            temp.pop()  # 앞에 (가 열려있으니 짝 맞춰 지우기
    if len(temp) != 0:
        return False
    return True


# solution
def solution(p):
    if p == '' or right(p):  # 1.입력이 빈 문자열인 경우 빈 문자열을 반환합니다.& 바로 올바른 경우 return
        return p

    u, v = p[:balanced(p) + 1], p[balanced(p) + 1:]  # 2.문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.

    if right(u):  # 3.문자열 u가 "올바른 괄호 문자열" 이라면
        return u + solution(v)  # 3-1.문자열 v에 대해 1단계부터 다시 수행 /수행한 결과 문자열을 u에 이어 붙인 후 반환

    else:  # 4.문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
        temp = '('  # 4-1.빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        temp += solution(v)  # 4-2.문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        temp += ')'  # 4-3.')'를 다시 붙입니다.
        # 4-4.u의 첫 번째와 마지막 문자를 제거하고 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        u = u[1:-1].replace('(', 'a')
        u = u.replace(')', 'b')
        u = u.replace('a', ')')
        u = u.replace('b', '(')
        return temp + u  # 4-5.생성된 문자열을 반환합니다.


print(solution(')('))
