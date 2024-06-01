def solution(arr, delete_list):
    answer = []
    for i in range(len(arr)):
        for j in range(len(delete_list)):
            if(arr[i] == delete_list[j]):
                break
            if(j == len(delete_list) - 1):
                answer.append(arr[i])
    return answer