'''
#############################################################################################################

1. <<크레인 인형뽑기 게임>>

입출력 예
board	                                                        moves	            result
[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	[1,5,3,5,1,2,1,4]	4

##############################################################################################################

'''

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