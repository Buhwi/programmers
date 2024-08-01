def solution(elements):
    arr = []
    elen = len(elements)
    for i in range(elen):
        temp = elements[i]
        for j in range(i, i+elen):
            arr.append(temp)
            temp = temp + elements[(j+1)%elen]
    return len(list(set(arr)))