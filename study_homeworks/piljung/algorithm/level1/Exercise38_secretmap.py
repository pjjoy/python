# 38. [1차]비밀지도


def solution(n, arr1, arr2):
    maparr1 = [str(bin(x)[2:].zfill(n)) for x in arr1]  # 이진수로 변환
    maparr2 = [str(bin(y)[2:].zfill(n)) for y in arr2]
    answer = []

    for i in range(n):
        ans = ''
        for j in range(n):
            ans = ans + (' ' if maparr1[i][j] == '0' and maparr2[i][j] == '0' else '#')  # 문자열로 더하기
        answer.append(ans)

    return answer