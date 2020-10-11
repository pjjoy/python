# 8. 문자열 압축 (직접 풀수 있도록 연습하기)

def solution(s):
    length = []
    result = ""

    if len(s) == 1:
        return 1
    for cut in range(1, len(s) // 2 + 1):
        count = 1
        tempStr = s[:cut]
        print(cut)

        for i in range(cut, len(s), cut):  # range(start, stop, step)
            # if-else문에서 잘린 한 cut 단위가 얼마 반복되는지 확인 후 result에 숫자+cut단위 붙여 담기
            if s[i:i + cut] == tempStr:
                count += 1
            else:
                if count == 1:
                    count = ""
                result += str(count) + tempStr
                tempStr = s[i:i + cut]
                count = 1
                print(result)
        # (마무리) count가 1로 마지막에 돈 경우에는 count 없이 그대로 붙이고 있는 경우는 숫자 해서 붙이기
        if count == 1:
            count = ""
        result += str(count) + tempStr
        length.append(len(result))
        result = ""  # 초기화
    print(length)
    return min(length)