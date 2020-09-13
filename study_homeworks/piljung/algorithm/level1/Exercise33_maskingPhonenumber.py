# 33. 핸드폰 번호 가리기

def solution(x):
    strx = str(x)
    sum = 0

    for i in range(len(strx)):
        sum += int(strx[i])

    return True if x % sum == 0 else False