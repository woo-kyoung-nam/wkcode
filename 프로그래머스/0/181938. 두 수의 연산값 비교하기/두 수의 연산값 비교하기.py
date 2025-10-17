def solution(a, b):
    answer = 0
    
    ab2 = 2*a*b
    str_a = str(a)
    str_b = str(b)
    str_ab = str_a + str_b
    
    if ab2 < int(str_ab) or ab2 == int(str_ab):
        answer = str_ab
    elif ab2 > int(str_ab):
        answer = ab2
    # elif ab2 == int(str_ab):
    #     answer = 
    
    return int(answer)