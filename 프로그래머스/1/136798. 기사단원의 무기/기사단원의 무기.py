def solution(number, limit, power):
    temp = []
    for i in range(1, number+1):
        m = bu(i)
        print(m)
        if m > limit:
            temp.append(power)
        else:
            temp.append(m)
    return sum(temp)
        
def bu(n):
    sum = 0

    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            sum += 1
            if n//i != i:
                sum += 1
    return sum