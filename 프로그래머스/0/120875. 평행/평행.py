def solution(dots):
    for i in range(3):
        if gradient(dots[(i%4)], dots[(i+1)%4], dots[(i+2)%4], dots[(i+3)%4]) == 1:
            return 1
        
    return 0

def gradient(dot1, dot2, dot3, dot4):
    g1 = (dot2[1] - dot1[1]) / (dot2[0] - dot1[0])
    g2 = (dot4[1] - dot3[1]) / (dot4[0] - dot3[0])
    return 1 if g1 == g2 else 0