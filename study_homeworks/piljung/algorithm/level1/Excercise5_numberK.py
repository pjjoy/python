def solution(array, commands):
    answer = []

    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]

        slice = array[i - 1:j]  # i<=  < j
        slice.sort()

        answer.append(slice[k - 1])
