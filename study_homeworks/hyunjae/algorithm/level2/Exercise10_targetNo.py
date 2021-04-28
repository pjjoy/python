import collections
def solution(numbers, target):
    queue = collections.deque([(0,0)])
    answer = 0
    while queue:
        current_value, index = queue.popleft()
        if index == len(numbers):
            if current_value == target:
                answer += 1
        else:
            queue.append((current_value + numbers[index], index + 1))
            queue.append((current_value - numbers[index], index + 1))
    return answer

def solution(numbers, target):
    print(numbers,target)
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

number = [1,1,1,1,1]
target = 3
print(solution(number,target))