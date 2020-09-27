# 41. 두 개 뽑아서 더하기

def solution(numbers):
    sumlist = []

    for m in range(len(numbers)):
        for n in range(len(numbers)):
            if m != n:
                sumlist.append(numbers[m] + numbers[n])

    answer = sorted(list(set(sumlist)))  # 리스트 중복 제거 : list를 set으로 변형했다가 다시 list로

    return answer