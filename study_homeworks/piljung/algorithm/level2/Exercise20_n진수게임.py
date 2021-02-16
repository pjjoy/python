# 20. N진수 게임 (2018 kakao blind recruitment)


def convert(n, base):
    arr = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return arr[r]
    else:
        return convert(q, base) + arr[r]


def solution(n, t, m, p):
    answer = ''
    all_answer = []

    for i in range(t * m):
        conv = convert(i, n)
        for c in conv:
            all_answer.append(c)

    # 튜브의 답만 추출
    for i in range(p - 1, t * m, m):
        answer += all_answer[i]

    return answer