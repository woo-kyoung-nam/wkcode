# slice : 피자 조각 수 (2조각~10조각)
# n : 피자 먹는 사람의 수

def solution(slice, n):
    answer = 0
    if n % slice == 0:
            answer = n // slice
    else:
            answer = n // slice +1
    return answer