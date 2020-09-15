# 30. 콜라츠 추측


def solution(num):
    answer = 0

    while num > 1:
        if answer == 500:
            answer = -1
            break
        else:
            answer += 1

            if num % 2 == 0:
                num = num // 2
            else:
                num = (num * 3) + 1

    return answer