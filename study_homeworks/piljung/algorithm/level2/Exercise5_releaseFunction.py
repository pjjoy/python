# 4. 기능개발

def solution(progresses, speeds):
    time = []
    answer = []

    for n in range(len(progresses)):  # 작업 별 소요 시간(time) 계산
        W = progresses[n]
        day = 0
        while W < 100:
            W += speeds[n]
            day += 1
        time.append(day)

    front = 0  # 배포일 계산
    for idx in range(len(time)):
        if time[front] < time[idx]:
            answer.append(idx - front)
            front = idx
    answer.append(len(time) - front)

    return answer