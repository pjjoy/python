# 9. 큰 수 만들기
    # 10번 문제 런타임 에러
    # 12번 문제 실패 ( 10000,2 넣어서 해답 찾기)

def solution(number, k):
    answer = ''

    while k > 0:

        answer += max(number[:k+1])
        i = number[:k+1].find(max(number[:k+1]))
        k = k - i
        number = str(number[i + 1:])

        if k == len(number):
            break

    return answer +number



# 다른 분 정답 (스텍 큐 개념 이해하기)

def solution(number, k):
    stack = []

    for i in range(len(number)):
        if not stack:
            stack.append(number[i])
            continue

        isRemove = False

        while stack and int(stack[-1]) < int(number[i]):
            stack.pop()
            k -= 1
            if not k:
                isRemove = True
                stack += number[i:]
                break

        if isRemove:
            break

        stack.append(number[i])

    return "".join(stack[:len(number) - k]) if k else "".join(stack)