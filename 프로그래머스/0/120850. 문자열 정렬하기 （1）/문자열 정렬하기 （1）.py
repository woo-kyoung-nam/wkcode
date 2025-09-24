def solution(my_string):
    answer = []
    for i in my_string:
        if i.isdigit(): #문자열이 오직 숫자 문자(0-9)로만 구성되어 있는지 확인하여 True 또는 False를 반환
            answer.append(int(i))
    answer.sort()
    return answer