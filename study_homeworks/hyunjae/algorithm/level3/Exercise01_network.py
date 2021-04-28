from collections import deque
def solution(n, computers):
    network = 0
    queue = deque()
    visit = [False for _ in range(n)]

    for idx_1, i in enumerate(visit):
        if not i:
            if not queue:
                queue.append(computers[idx_1])
                visit[idx_1] = True
            while queue:
                for idx, i in enumerate(queue[0]):
                    if idx != idx_1 and (not visit[idx]) and i == 1:
                        queue.append(computers[idx])
                        visit[idx] = True
                queue.popleft()
            network += 1
    return network


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
n = 4
computers = [[1, 0, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
print(solution(n, computers))