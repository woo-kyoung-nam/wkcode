# array = 머쓱이네 반 친구들의 키가 담긴 정수 배열
# height 머쓱이의 키
# Q = 머쓱이보다 키 큰 사람 수
# R = array를 순회하며 조건문을 통해 1씩 증가 또는 0씩 증가

def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
        else:
            answer += 0
    return answer