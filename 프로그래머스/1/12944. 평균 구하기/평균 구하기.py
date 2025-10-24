def solution(arr):
    answer = 0
    a = 0
    for i in arr:
        a += i
        b = len(arr)
        answer = a/b
    return answer