def solution(num_list):
    answer = 0
    answer1 = 0
    
    for i in num_list:
        if i % 2:
            answer = answer*10+i
        else:
            answer1 = answer1*10+i
                
    return answer+answer1