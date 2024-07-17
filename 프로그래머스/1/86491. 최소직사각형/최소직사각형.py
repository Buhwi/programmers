def solution(sizes):
    w = []
    h = []
    for i in range(len(sizes)):
        w.append(sorted(sizes[i])[0])
        h.append(sorted(sizes[i])[1])
    return max(w)*max(h)