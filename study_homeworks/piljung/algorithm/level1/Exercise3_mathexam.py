def solution(answers):
    oneanswer = [1, 2, 3, 4, 5]
    twoanswer = [2, 1, 2, 3, 2, 4, 2, 5]
    threeanswer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    answer = []

    for i in range(len(answers)): # 나눗셈 나머지 위치 값으로 규칙가져오기 (+ 세가지 값 함께 하나의 for문에서 설정하는 아이디어 기억하기)
        if answers[i] == oneanswer[i % len(oneanswer)]:
            scores[0] += 1
        if answers[i] == twoanswer[i % len(twoanswer)]:
            scores[1] += 1
        if answers[i] == threeanswer[i % len(threeanswer)]:
            scores[2] += 1

    max_score = max(scores)
    for i in range(3):
        if scores[i] == max_score:
            answer.append(i + 1) # 하나씩 max_score를 가진 수포자 응시자 더하기

    return answer