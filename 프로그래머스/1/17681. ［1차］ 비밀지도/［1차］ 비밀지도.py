def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append(str(int(bin(arr1[i])[2::]) + int(bin(arr2[i])[2::])))
        if len(answer[i]) < n:
            answer[i] = "0"*(n-len(answer[i])) + answer[i]
        
        answer[i] = answer[i].replace("1", "#").replace("2", "#").replace("0", " ")
        
    return answer