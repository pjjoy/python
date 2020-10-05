# 40. [1차] 다트게임

import re


def solution(dartResult):
    scores = re.findall('\d+', dartResult)  # 숫자만 추출하는 방법
    bonuses = re.findall("[a-zA-Z,*,#]+", dartResult)  # 문자만 추출하는 방법
    ans = []  # 조건 적용한 각 요소 값을 넣기

    for x in range(0, len(bonuses)):
        if bonuses[x][0] == 'S':
            if len(bonuses[x]) == 2 and bonuses[x][1] == '*':  # * : 두배 (해당점수, 직전 점수)
                ans.append(int(scores[x]) ** 1 * 2)
                if x != 0:
                    ans[x - 1] = ans[x - 1] * 2
            elif len(bonuses[x]) == 2 and bonuses[x][1] == '#':  # #: 마이너스 (해당점수)
                ans.append(int(scores[x]) ** 1 * (-1))
            else:
                ans.append(int(scores[x]) ** 1)

        elif bonuses[x][0] == 'D':
            if len(bonuses[x]) == 2 and bonuses[x][1] == '*':
                ans.append(int(scores[x]) ** 2 * 2)
                if x != 0:
                    ans[x - 1] = ans[x - 1] * 2
            elif len(bonuses[x]) == 2 and bonuses[x][1] == '#':
                ans.append(int(scores[x]) ** 2 * (-1))
            else:
                ans.append(int(scores[x]) ** 2)

        else:
            if len(bonuses[x]) == 2 and bonuses[x][1] == '*':
                ans.append(int(scores[x]) ** 3 * 2)
                if x != 0:
                    ans[x - 1] = ans[x - 1] * 2
            elif len(bonuses[x]) == 2 and bonuses[x][1] == '#':
                ans.append(int(scores[x]) ** 3 * (-1))
            else:
                ans.append(int(scores[x]) ** 3)

                # print(scores)
    # print(bonuses)
    # print(ans)

    return sum(ans)