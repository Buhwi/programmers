from collections import Counter

def solution(k, tangerine):
    answer = 0
    arr = sorted(list((dict(Counter(tangerine))).values()), reverse=True)
    
    while k > 0:
        k -= arr[answer]
        answer += 1
    
    return answer