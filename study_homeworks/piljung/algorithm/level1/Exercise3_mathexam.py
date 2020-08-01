'''
#############################################################################################################
3. <<모의고사>>

##문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

##제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

##입출력 예
answers     	return
[1,2,3,4,5]	    [1]
[1,3,2,4,2]	    [1,2,3]

'''

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