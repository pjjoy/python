def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekday = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    diff = b - 1

    for i in range(a - 1):
        diff += month[i]   # 0~365(윤년)일 중 해당 일자가 몇번째 일자인지 체크

    return weekday[diff % 7]
