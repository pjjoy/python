#13. 순위 검색 (2021 KAKAO BLIND RECRUITMENT)

# 필터 조건이 맞을때 1을 반환하는 함수
def chk_sync(candidate, chk_cond):
    i = 0
    while i < 4:
        if chk_cond[i] != '-' and candidate[i] == chk_cond[i]:
            i += 1
        elif chk_cond[i] == '-':
            i += 1
        else:
            break
    return (1 if i == 4 else 0)


# 문제의 solution 함수
def solution(info, query):
    candidate_list = []
    array_info = []
    array_query = []
    answer = []

    # 이중 리스트로 조건 정리
    for i in info:
        array_info.append(i.split())

    for j in query:
        cond = j.split()
        while 'and' in cond:
            cond.remove('and')  # 'and' 삭제
        array_query.append(cond)

    # print(array_query)
    # print(array_info)

    # 조건 일치 지원자 수 체크
    for a in array_query:  # 조건
        # print(a)
        ans = 0
        for b in array_info:  # 지원자
            # print(b)
            # print(b[4])
            # print(a[4])
            # print(chk_sync(b,a[:4]))
            # print(chk_sync(b,a) if int(b[4])>=int(a[4]) else 0)
            ans += (chk_sync(b, a) if int(b[4]) >= int(a[4]) else 0)  # 점수 조건이 충족하는 사람만, 지원 항목 맞는지 chk_sync 함수로 체크

        answer.append(ans)

    return answer