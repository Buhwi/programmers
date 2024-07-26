def solution(arr):
    answer = 0
    k = 1
    temp = max(arr)
    
    while True:
        count = 0
        for i in arr:
            if (temp*k) % i == 0:
                count += 1
        if count == len(arr):
            answer = temp*k
            break
        k += 1
    
    return answer