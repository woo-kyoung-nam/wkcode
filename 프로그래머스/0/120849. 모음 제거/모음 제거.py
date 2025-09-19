def solution(my_string):
    # answer = ""
    mo = ("a","e","i","o","u")
    for i in mo:
        my_string = my_string.replace(i, "")
    
    return my_string
