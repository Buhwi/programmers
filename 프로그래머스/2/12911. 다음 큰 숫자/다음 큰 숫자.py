def solution(n):
    m = str(bin(n)).count("1")
    while(True):
        n += 1
        if m == str(bin(n)).count("1"):
            break

    return n