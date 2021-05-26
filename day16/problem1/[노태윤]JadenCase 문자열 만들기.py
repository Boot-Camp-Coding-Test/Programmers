def solution(s):
    splitted = s.split(" ")
    modified_list = list(map(lambda x : x.lower().capitalize(),splitted))
    answer = " ".join(modified_list)
    return answer
