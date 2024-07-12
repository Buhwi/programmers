def solution(s):
    dic = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(dic)):
        s = s.replace(dic[i], str(i))

    return int(s)