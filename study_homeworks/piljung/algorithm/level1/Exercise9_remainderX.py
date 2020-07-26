def solution(arr, divisor):
    answer = []
    sortarr = arr.sort()

    for arri in arr:
        if arri % divisor == 0:
            answer.append(arri)
        else:
            continue

    if len(answer) == 0:
        answer.append(-1)

    return answer