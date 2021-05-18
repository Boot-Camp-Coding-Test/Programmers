def solution(phone_number):
    x = len(list(phone_number))
    return '*'*(x-4)+phone_number[-4:]
