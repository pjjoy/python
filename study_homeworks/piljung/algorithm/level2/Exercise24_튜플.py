# 24. 튜플

def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key=len)

    # for i in s:
    for x in s:
        y = x.split(",")
        for z in y:
            if int(z) not in answer:
                answer.append(int(z))

    return answer


'''
import re

def solution(s):
    answer = []
    a = s.split(',{')
    a.sort(key = len)
    for j in a:
        numbers = re.findall("\d+", j)
        for k in numbers:
            if int(k) not in answer:
                answer.append(int(k))
    return answer
'''