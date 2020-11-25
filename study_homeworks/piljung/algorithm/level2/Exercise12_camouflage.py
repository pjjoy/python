#12. 위장

def solution(clothes):
    closet = {}
    result = 1
    for element in clothes:
        key = element[1]
        if key in closet:
            closet[key]+=1
        else:
            closet[key]=1
    print(closet)
    for key in closet.keys():
        result = result * (closet[key] + 1) #(a+1)(b+1)....-1
    return result - 1