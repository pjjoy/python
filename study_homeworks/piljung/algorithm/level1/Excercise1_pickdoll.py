def solution(board, moves):
    basket = []
    answer = 0
    kkofriend = 0

    for move in moves:
        for i in range(len(board)): # 열 수 기준
            if board[i][move - 1] > 0:
                kkofriend = board[i][move - 1] # 집은 인형 세팅
                board[i][move - 1] = 0 # 인형있던 자리 비우기

                if len(basket) > 0 and basket[-1] == kkofriend:  # 마지막=새로운거
                    answer += 2  # 사라진 결과값 더하기
                    basket.pop()  # 리스트에서 마지막 항목 삭제
                else:
                    basket.append(kkofriend)  # 리스트 마지막 항목에 더하기
                break
    return answer