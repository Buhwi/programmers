def solution(n):
    ans = 0
    while n >= 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n // 2
            ans += 1
    return ans
