def solution(phone_number):
    answer = ''

    for i in range(len(phone_number) - 4):
        answer += '*'
    
    num_lst = [i for i in phone_number][-4:]
    for n in num_lst:
        answer += n
    
    return answer


def solution(phone_number):
    answer = '*'*(len(phone_number)-4) + phone_number[-4:]
    return answer
