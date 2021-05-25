def solution(s):
    splitted = list(map(int,s.split(" ")))
    answer = str(min(splitted)) + ' ' + str(max(splitted))
    return answer
