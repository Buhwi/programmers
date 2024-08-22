def solution(n):
    arr = [1, 2, 3]
    for i in range(3, n):
        arr.append(arr[i-1] + arr[i-2])     
    
    return (arr[n-1] % 1234567)