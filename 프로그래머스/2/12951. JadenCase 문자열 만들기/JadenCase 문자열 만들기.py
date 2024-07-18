def solution(s):
    arr = s.lower().split(" ")
    answer = ""
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j == 0:
                answer+=arr[i][j].upper()
            else:
                answer+=arr[i][j]
        if i < len(arr)-1:
            answer+=" "
    return answer