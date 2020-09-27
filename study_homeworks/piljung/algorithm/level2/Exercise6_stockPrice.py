#6. 주식 가격

def solution(prices):
    answer = []

    for m in range(len(prices)):
        time = 0
        for n in range(m + 1, len(prices)):
            time = time + 1
            if prices[m] > prices[n]:
                break
        answer.append(time)
    return answer