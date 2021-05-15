import math

def solution(n):
    answer = ''
    watermelon = '수박'
    watermelon = watermelon*(math.ceil(n/2))
    
    return watermelon[:n]