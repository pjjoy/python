## 참고
## set>list : 중복 제거 가능  newarr = list(set(arr))

def solution(arr):
    answer = []
    answer.append(arr[0])

    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            answer.append(arr[i])

    return answer