#23. 자연수 뒤집어 배열로 만들기
def solution(n):
    new_n=reversed(str(n))
    answer = []
    for i in new_n:
        answer.append(int(i))
    return answer

def solution(n):
	return [int(i) for i in str(n)][::-1]