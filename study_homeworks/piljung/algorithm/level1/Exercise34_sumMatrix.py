# 34. 행렬의 덧샘

def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]  # 더해서 새로운 list 만들필요 없음 answer[[]] X arr에 요소 바로 더하기

    return arr1