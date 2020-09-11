# 29. 최대공약수와 최소 공배수

# a,b  의 최대공약수는 (a%b),b 의 최대공약수와 같다.
# 최소공배수는 a과 b의 곱에 최대공약수를 나누어 준 것과 같다.

def solution(n, m):
    a = n
    b = m

    mod = a % b
    while mod > 0:
        a, b = b, mod
        mod = a % b

    return [b, m * n // b]