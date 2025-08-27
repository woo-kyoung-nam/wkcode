def solution(sides):
    answer = 0
    num = sorted(sides)
    
    if num[0]+num[1] > num[2]:
        answer = 1
    elif num[0]+num[1] == num[2] or num[0]+num[1] < num[2]:
        answer = 2
        
    return answer