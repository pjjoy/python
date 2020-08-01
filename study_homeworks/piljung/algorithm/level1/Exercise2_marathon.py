'''
#############################################################################################################
2. <<완주하지 못한 선수>>

[문제 설명]
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

[제한사항]
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.

[입출력 예]
participant	                                completion	                            return
[leo, kiki, eden]	                        [eden, kiki]	                        leo
[marina, josipa, nikola, vinko, filipa]	    [josipa, filipa, marina, nikola]	    vinko
[mislav, stanko, mislav, ana]	            [stanko, ana, mislav]	                mislav

##############################################################################################################
'''
def solution(participant, completion):
    for man in completion:
        participant.remove(man) # 완주자를 참가자에서 제외하기
        answer = participant[0] # 항상 1명만 완주하지 못한것이므로 다 제외하고 남은 하나의 원소(?) 추출
    return answer

##효율성 높일 필요 있음

'''
#다른 풀이 1
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


#다른 풀이 2
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
'''