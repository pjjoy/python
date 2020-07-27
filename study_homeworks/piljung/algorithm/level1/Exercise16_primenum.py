#16. 소수 찾기

def solution(n):
    answer = 0
    for x in range(2, n+1):
        for j in range(2, x):
            if x % j == 0:
                break   #아무것도 안하고 넘어감
            else:
                answer += 1
    return answer


## 효율성 문제...