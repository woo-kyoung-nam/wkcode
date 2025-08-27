def solution(num_list):
    answer = []
    fir,sec = 0,0
    
    for i in num_list:
        if i % 2 == 0:
            fir += 1
        elif i % 2 != 0:
            sec += 1
            
    answer = [fir,sec]
    return answer