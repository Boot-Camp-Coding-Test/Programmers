def solution(strings, n):
    strings = sorted(strings)
    sorted_lst =  sorted(strings, key=lambda x: x[n])

    return sorted_lst
