def solution(n, lost, reserve):
    reserve_set = set(reserve)-set(lost)
    lost_set = set(lost)-set(reserve)
    
    for r in reserve_set:
        if r-1 in lost_set:
            lost_set.remove(r-1)
        elif r+1 in lost_set:
            lost_set.remove(r+1)
            
    return n-len(lost_set)


# 1
# 1->2
# 3
# 3->4 or 5->4
# 5


# 1
# 3->2 or 3->4
# 3
# 5

# 1
# 2