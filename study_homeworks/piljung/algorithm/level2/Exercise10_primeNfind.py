# 10. 소수찾기

import itertools  # 순열 쓰기 위해 라이브러리 사용


def solution(numbers):
    answer = 0
    listnum = list(numbers)  # 숫자 쪼개기
    newnums = []

    # 숫자 조합 만들기
    for i in range(1, len(numbers) + 1):
        newnums += list(map(''.join, itertools.permutations(numbers, i)))  # 순열

    checkprime = list(set(int(a) for a in newnums))  # 정수화, 중복제거

    # 소수판별 함수 생성
    def is_prime_ornot(n):
        if n < 2:
            return False
        for i in range(2, n):
            if n % i is 0:
                return False
        return True

    # 소수판별
    for a in checkprime:
        if is_prime_ornot(a) == True:
            answer += 1

    return answer