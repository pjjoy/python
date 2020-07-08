def solution(participant, completion):
    for man in completion:
        participant.remove(man) # 완주자를 참가자에서 제외하기
        answer = participant[0] # 항상 1명만 완주하지 못한것이므로 다 제외하고 남은 하나의 원소(?) 추출
return answer