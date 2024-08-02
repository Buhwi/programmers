def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        answer.append(i//n+1 if i//n+1 >= i%n+1 else i%n+1)
    return answer

#arr[몫열][나머지]
    