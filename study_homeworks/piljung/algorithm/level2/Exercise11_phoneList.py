#11. 전화번호 목록 (효율성 문제)

def solution(phone_book):
    sortset = sorted(phone_book, key=len)
    answer = True
    for i in range(len(sortset)):
        for j in range(i + 1, len(sortset)):
            if sortset[i] == sortset[j][0:len(sortset[i])]:
                answer = False

    return answer