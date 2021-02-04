# 14.  더 맵게

import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0]<K :
        if len(scoville)>1:  # 1개 있을때 굳이 돌릴 필요 없음... break하고 마무리하는게 좋음
            a=heapq.heappop(scoville)
            b=heapq.heappop(scoville)
            heapq.heappush(scoville, a+b*2)
            answer+=1
        else:
            answer=-1
            break
    return answer