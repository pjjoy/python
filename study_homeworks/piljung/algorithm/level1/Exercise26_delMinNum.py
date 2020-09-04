# 26. 제일 작은 수 제거하기

def solution(arr):
    if len(arr) > 1 :
        arr.remove(min(arr))  #arr.pop(arr.index(min(arr)))
        return arr
    else :
        return [-1]