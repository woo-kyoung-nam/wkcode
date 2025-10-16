def solution(a, b):
    answer = 0
    a_str = str(a)
    b_str = str(b)
    
    ab_str = a_str + b_str
    ba_str = b_str + a_str
    if int(ab_str) < int(ba_str):
        answer = ba_str
    elif int(ab_str) > int(ba_str):
        answer = ab_str
    elif int(ab_str) == int(ba_str):
        answer = ab_str
        
    return int(answer)