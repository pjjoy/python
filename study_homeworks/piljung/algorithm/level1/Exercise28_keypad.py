# 28. [카카오 인턴] 키패드 누르기

def solution(numbers, hand):
    result = []
    d = {[1, 2]: 1, [3, 2]: 1, [4, 2]: 2, [6, 2]: 2, [7, 2]: 3, [9, 2]: 3,
         [1, 5]: 2, [3, 5]: 2, [4, 5]: 1, [6, 5]: 1, [7, 5]: 2, [9, 5]: 2,
         [1, 8]: 3, [3, 8]: 3, [4, 8]: 2, [6, 8]: 2, [7, 8]: 1, [9, 8]: 1,
         [1, 0]: 4, [3, 0]: 4, [4, 0]: 3, [6, 0]: 3, [7, 0]: 2, [9, 0]: 2}  ##[앞숫자: 뒷숫자] 거리
    Left = "*"
    Right = "#"

    if numbers[0] in (2, 5, 8, 0):
        result.append("L" if hand == "left" else "R")

    else:
        for i in range(len(numbers)):
            if numbers[i] in (1, 4, 7):
                result.append("L")
                Left = numbers[i]
            elif numbers[i] in (3, 6, 9):
                result.append("R")
                Right = numbers[i]
            else:
                if number[i - 1]

    answer = ''
    return answer