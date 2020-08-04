#2. 프린터

#sol 1) 가장 쉽게 이해할 수 있었던 답

def solution(priorities, location):
    answer = 0
    bin = []
    for idx, val in enumerate(priorities):
        bin.append((idx,val))       # 프린트 순위와 중요도를 튜플화

    while bin:
        idx,val = bin.pop(0)
        if max(priorities) > val:
            bin.append((idx,val))    # 앞에서 없애고 뒤에 더함함
       else:
            answer+=1
            priorities.remove(val)
            if idx == location:
                break
    return answer


#sol 2) 많은 답안의 방법
def solution(priorities, location):
    answer = 1
    pqueue = [(i, j) for i, j in enumerate(priorities)]  # 프린트 순위와 중요도를 튜플화 (0, 2)
    answers = []

    # pqueue에 있는 작업들을 조건에 맞게 재배치할 때까지
    while pqueue:

        count = len(pqueue)
        prior = pqueue.pop(0)

        # 제일 처음 작업의 기여도가 다른 작업의 기여도보다 낮으면
        # 다시 pqueue 제일 뒤로 추가
        for i in range(len(pqueue)):
            if prior[1] < pqueue[i][1]:
                pqueue.append(prior)
                break

        # 만약 제일처음 pqueue의 갯수와 값이 같은 경우는 위의 if문을 실행한 경우
        if count == len(pqueue):
            continue

        # 그렇지 않으면 제일 먼저 프린트하게 되는 경우로 새로운 리스트에 처음으로 추가
        else:
            answers.append(prior)

    # while문이 끝난 뒤 프린트하고자한 location이 몇번째로 프린트하게 됬는 지 판단
    for i in answers:
        if i[0] == location:
            break
        else:
            answer += 1

    return answer