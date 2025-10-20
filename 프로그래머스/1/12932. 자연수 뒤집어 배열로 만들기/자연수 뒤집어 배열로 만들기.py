def solution(n):
    answer = []
    n_list = list(str(n))
    n_list.reverse()
    return list(map(int,n_list))