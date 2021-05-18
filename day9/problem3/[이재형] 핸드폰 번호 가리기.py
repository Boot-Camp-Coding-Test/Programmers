def solution(phone_number):
    a = '*'
    return a*(len(phone_number)-4) + phone_number[len(phone_number)-4:]
