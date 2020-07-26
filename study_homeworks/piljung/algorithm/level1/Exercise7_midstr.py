def solution(s):
    if len(s) % 2 == 1:
        answer = s[int(len(s) / 2)]
    else:
        answer = s[int(len(s) / 2 - 1): int(len(s) / 2 + 1)]

    return answer


## 슬라이싱으로 한번에 해결하기

def solution(s):
    return s[(len(s) - 1) // 2:len(s) // 2 + 1]

