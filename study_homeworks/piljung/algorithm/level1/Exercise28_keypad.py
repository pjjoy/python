# 28. [카카오 인턴] 키패드 누르기
import math
def solution(numbers, hand):
    result = []
    location = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                '4': (1, 0), '5': (1, 1), '6': (1, 2),
                '7': (2, 0), '8': (2, 1), '9': (2, 2),
                '*': (3, 0), '0': (3, 1), '#': (3, 2)} # 키패드 좌표

    Lhand, Rhand = '*', '#'

    for number in numbers:
        if number in (1, 4, 7):     # 좌측 숫자는 왼손으로
            result.append('L')
            Lhand = str(number)     # location 검색할 때 형변환 문제가 있어서 str로 형변환
        elif number in (3, 6, 9):   # 우측 숫자는 오른손으로
            result.append('R')
            Rhand = str(number)
        else:                       # 거리 계산 후 손 결정
            x_Lhand, y_Lhand = location[Lhand]
            x_Rhand, y_Rhand = location[Rhand]
            x_number, y_number = location[str(number)]  #좌표 정의

            if abs(x_Lhand - x_number) + abs(y_Lhand - y_number) == abs(x_Rhand - x_number) + abs(y_Rhand - y_number): # 거리 같으면 hand 따라
                if hand == 'left':
                    result.append('L')
                    Lhand = str(number)
                else:
                    result.append('R')
                    Rhand = str(number)

            elif abs(x_Lhand - x_number) + abs(y_Lhand - y_number) < abs(x_Rhand - x_number) + abs(y_Rhand - y_number):
                result.append('L')
                Lhand = str(number)
            else:
                result.append('R')
                Rhand = str(number)

    return "".join(result)  # 리스트로 안하고 바로 result='' / result+='L or R' 해도 됨


'''
 [함수 두개 생성해서 구하기기]
 
 def get_distance(hand, number):
    location = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                '4': (1, 0), '5': (1, 1), '6': (1, 2),
                '7': (2, 0), '8': (2, 1), '9': (2, 2),
                '*': (3, 0), '0': (3, 1), '#': (3, 2)}
    number = str(number)
    x_hand, y_hand = location[hand]
    x_number, y_number = location[number]
    return abs(x_hand - x_number) + abs(y_hand - y_number)

def solution(numbers, hand):
    answer = ''
    left, right = '*', '#'
    hand = 'R' if hand == 'right' else 'L'
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left = str(number)
            continue
        if number in [3, 6, 9]:
            answer += 'R'
            right = str(number)
            continue
        if number in [2, 5, 8, 0]:
            dis1 = get_distance(left, number)
            dis2 = get_distance(right, number)
            if dis1 > dis2:
                answer += 'R'
                right = str(number)
            if dis1 < dis2:
                answer += 'L'
                left = str(number)
            if dis1 == dis2:
                answer += hand
                if hand == 'R':
                    right = str(number)
                if hand == 'L':
                    left = str(number)
    return answer

'''