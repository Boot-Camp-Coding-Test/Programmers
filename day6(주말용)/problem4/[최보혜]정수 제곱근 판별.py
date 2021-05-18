def solution(n):
    answer = n**0.5
    if answer == int(n**0.5):
        return (answer+1)**2
    else:
        return -1
